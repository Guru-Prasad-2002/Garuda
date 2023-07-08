import cv2
import os
import face_recognition

def collect_data(subfoldarename):
# Set the directory path to store the face images
    known_dir = "Known"
    subfolder_name = subfoldarename # Change this to the desired subfolder name
    # Create the subfolder if it doesn't exist
    subfolder_path = os.path.join(known_dir, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

    # Initialize webcam
    video_capture = cv2.VideoCapture(1)

    # Face detection parameters
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Counter to keep track of the number of captured images
    image_counter = 0

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces using haarcascade
        # faces_haarcascade = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Detect faces using face_recognition library
        face_locations = face_recognition.face_locations(frame,model="hog")
        faces_face_recognition = len(face_locations)

        # Draw bounding boxes around the detected faces from haarcascade
        # for (x, y, w, h) in faces_haarcascade:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw bounding boxes around the detected faces from face_recognition library
        # if len(face_locations) == 1:
        #     for (top, right, bottom, left) in face_locations:
        #         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the resulting image
        cv2.imshow('Collecting Faces', frame)

        # Capture and save face images when both haarcascade and face_recognition detect faces
        if  len(face_locations) == 1:
        # if len(faces_haarcascade) == 1:
        # Increment the image counter
            image_counter += 1

            # Save the face image
            face_image_path = os.path.join(subfolder_path, f"{image_counter}.jpg")
            cv2.imwrite(face_image_path, frame)

            print(f"Captured image {image_counter}")

        # Exit loop when 100 images are captured or 'q' is pressed
        if image_counter >= 50 or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy the windows
    video_capture.release()
    cv2.destroyAllWindows()



# import cv2
# import os

# # Set the directory path to store the face images
# known_dir = "Known"
# subfolder_name = "Guru1"  # Change this to the desired subfolder name

# # Create the subfolder if it doesn't exist
# subfolder_path = os.path.join(known_dir, subfolder_name)
# os.makedirs(subfolder_path, exist_ok=True)

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Face detection parameters
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # Counter to keep track of the number of captured images
# image_counter = 0

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw bounding boxes around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # Display the resulting image
#     cv2.imshow('Collecting Faces', frame)

#     # Capture and save face images when 's' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('s') and len(faces) == 1:
#         # Increment the image counter
#         image_counter += 1

#         # Save the face image
#         face_image_path = os.path.join(subfolder_path, f"{image_counter}.jpg")
#         cv2.imwrite(face_image_path, frame)

#         print(f"Captured image {image_counter}")

#     # Exit loop when 50 images are captured or 'q' is pressed
#     if image_counter >= 50 or cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     print("Here")
# # Release the webcam and destroy the windows
# video_capture.release()
# cv2.destroyAllWindows()








# import cv2
# import os

# # Set the directory path to store the face images
# known_dir = "Known"
# subfolder_name = "Guru1"  # Change this to the desired subfolder name

# # Create the subfolder if it doesn't exist
# subfolder_path = os.path.join(known_dir, subfolder_name)
# os.makedirs(subfolder_path, exist_ok=True)

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Face detection parameters
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # Counter to keep track of the number of captured images
# image_counter = 0

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw bounding boxes around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # Display the resulting image
#     cv2.imshow('Collecting Faces', frame)

#     # Capture and save face images when 's' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('s') and len(faces) == 1:
#         # Increment the image counter
#         image_counter += 1

#         # Save the face image
#         face_image_path = os.path.join(subfolder_path, f"{image_counter}.jpg")
#         cv2.imwrite(face_image_path, frame)

#         print(f"Captured image {image_counter}")

#     # Exit loop when 50 images are captured or 'q' is pressed
#     if image_counter >= 50 or cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     print("Here")
# # Release the webcam and destroy the windows
# video_capture.release()
# cv2.destroyAllWindows()



