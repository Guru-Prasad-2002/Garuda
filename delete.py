import pickle
with open("known_faces.pickle", "rb") as file:
        known_data = pickle.load(file)
known_encodings = known_data["encodings"]
known_names = known_data["names"]

print(known_data)