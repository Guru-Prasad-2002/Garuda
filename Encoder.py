import face_recognition
import os
import pickle

known_encodings = []
known_names = []

known_dir = "Known"

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

# Create a dictionary with known encodings and names
known_data = {"encodings": known_encodings, "names": known_names}

# Save the dictionary as a pickle file
with open("known_faces.pickle", "wb") as file:
    pickle.dump(known_data, file)