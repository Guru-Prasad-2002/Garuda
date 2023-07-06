import face_recognition
import os
import pickle

def run_this():
    known_encodings = []
    known_names = []

    known_dir = "Known"

    # Check if the pickle file already exists
    if os.path.exists("known_faces.pickle"):
        # Load existing data from the pickle file
        with open("known_faces.pickle", "rb") as file:
            known_data = pickle.load(file)
            known_encodings = known_data["encodings"]
            known_names = known_data["names"]

    # Iterate over each person's directory
    for person_dir in os.listdir(known_dir):
        person_path = os.path.join(known_dir, person_dir)
        if not os.path.isdir(person_path):
            continue

        # Get the person's name
        person_name = person_dir
        print(f"Processing {person_name}...")

        # Check if the person's name already exists in known_names
        if person_name in known_names:
            print(f"{person_name} is already present in the pickle file.")
            continue

        # Iterate over each image of the person
        for image_file in os.listdir(person_path):
            image_path = os.path.join(person_path, image_file)

            # Load the image and generate face encoding
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image, model="hog")
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

    print("Updated pickle file with new encodings and names.")




# import face_recognition
# import os
# import pickle

# def run_this():
#     known_encodings = []
#     known_names = []

#     known_dir = "Known"

#     # Iterate over each person's directory
#     for person_dir in os.listdir(known_dir):
#         person_path = os.path.join(known_dir, person_dir)
#         if not os.path.isdir(person_path):
#             continue

#         # Get the person's name
#         person_name = person_dir
#         print(f"Processing {person_name}...")

#         # Iterate over each image of the person
#         for image_file in os.listdir(person_path):
#             image_path = os.path.join(person_path, image_file)

#             # Load the image and generate face encoding
#             image = face_recognition.load_image_file(image_path)
#             face_locations = face_recognition.face_locations(image, model="hog")
#             if len(face_locations) > 0:
#                 # Generate face encoding for the first detected face
#                 encoding = face_recognition.face_encodings(image, face_locations)[0]
#                 # Append the encoding and name to the known lists
#                 known_encodings.append(encoding)
#                 known_names.append(person_name)
#             else:
#                 print(f"No face detected in {image_file}")

#     # Create a dictionary with known encodings and names
#     known_data = {"encodings": known_encodings, "names": known_names}
#     # print(known_data)

#     # Save the dictionary as a pickle file
#     with open("known_faces.pickle", "wb") as file:
#         pickle.dump(known_data, file)
#     with open("known_faces.pickle", "rb") as file:
#         known_data = pickle.load(file)
#         known_encodings = known_data["encodings"]
#         known_names = known_data["names"]
#         print(known_data)
#         print(known_names)

# run_this()