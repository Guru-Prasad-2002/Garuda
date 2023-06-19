# rename all files presnet in a folder Known/Guru1 from 1.jpg to 50.jpg to 51.jpg to 100.jpg

import os

folder_path = "Known/Guru1"  # Specify the folder path here

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)

    if os.path.isfile(filepath) and filename.endswith(".jpg"):
        # Extract the file number from the current filename
        file_number = int(filename.split(".")[0])

        if 1 <= file_number <= 50:
            # Calculate the new file number
            new_file_number = file_number + 50

            # Create the new filename
            new_filename = str(new_file_number) + ".jpg"

            # Construct the new filepath
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")
