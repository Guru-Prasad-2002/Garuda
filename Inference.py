import cv2
import face_recognition
import pickle
import os
from datetime import datetime
import subprocess

# Load known face encodings and their names from the pickle file
confidence_threshold = 0.5
unknown_counter = 0
save_unknown = False


with open("known_faces.pickle", "rb") as file:
    known_data = pickle.load(file)
known_encodings = known_data["encodings"]
known_names = known_data["names"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Create 'Unknown' folder if it doesn't exist
if not os.path.exists("Unknown"):
    os.makedirs("Unknown")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate over detected faces
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare the face encoding with known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        d={i:0 for i in known_names}
        # max_name=""
        # max_count=0
        for i in range(len(matches)):
            if matches[i]:
                face_distance = face_recognition.face_distance([known_encodings[i]], face_encoding)
                if face_distance[0] < confidence_threshold:
                    d[known_names[i]]+=1
        name=max(d,key=lambda x:d[x])
        print(name,d[name])
        if d[name]< 2:
            name="Unknown"
        
        # Draw bounding box and label on the frame
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        # Store image of unknown face
        if name == "Unknown":
            unknown_counter += 1
            if unknown_counter > 10:
                save_unknown = True
                unknown_counter = 0
        else:
            unknown_counter = 0
            save_unknown = False

        if save_unknown:
            unknown_counter = 0
            save_unknown = False
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            command = ['python', 'sms.py', "Unknown face detected at " + timestamp]
            image_name = f"Unknown/{timestamp}.jpg"
            cv2.imwrite(image_name, frame)
            subprocess.run(command)

    # Display the resulting image
    cv2.imshow('Face Recognition', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy the windows
video_capture.release()
cv2.destroyAllWindows()

