import cv2
import face_recognition
import os

# Load known face encodings and their names
known_encodings = []
known_names = []

known_dir = "Known1"

# Iterate over each person's directory
for person_dir in os.listdir(known_dir):
    person_path = os.path.join(known_dir, person_dir)
    if not os.path.isdir(person_path):
        continue

    # Get the person's name
    person_name = person_dir

    # Iterate over each image of the person
    for image_file in os.listdir(person_path):
        image_path = os.path.join(person_path, image_file)

        # Load the image and generate face encoding
        # image = face_recognition.load_image_file(image_path)
        # encoding = face_recognition.face_encodings(image)[0]
        image = face_recognition.load_image_file(image_path)   
        face_locations = face_recognition.face_locations(image)     
        if len(face_locations) > 0:
            # Generate face encoding for the first detected face
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            # Append the encoding and name to the known lists
            known_encodings.append(encoding)
            known_names.append(person_name)
        else:
            print(f"No face detected in {image_file}")

        # Append the encoding and name to the known lists
        known_encodings.append(encoding)
        known_names.append(person_name)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate over detected faces
    for face_encoding in face_encodings:
        # Compare the face encoding with known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # Check for any match
        if True in matches:
            matched_index = matches.index(True)
            name = known_names[matched_index]

        # Draw bounding box and label on the frame
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('Face Recognition', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy the windows
video_capture.release()
cv2.destroyAllWindows()
