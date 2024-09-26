import os

# Directory where your YOLOv8 annotations (.txt files) are stored
label_directory = r"C:\Users\VikasVarpe\Downloads\EgoHands Public.v1-specific.yolov81\labels\val"

# New class ID that you want to merge all labels into (e.g., '0')
new_class_id = 0

# Loop through all label files in the directory
for label_file in os.listdir(label_directory):
    if label_file.endswith(".txt"):
        label_path = os.path.join(label_directory, label_file)

        # Read the label file
        with open(label_path, "r") as file:
            lines = file.readlines()

        # Open the label file for writing
        with open(label_path, "w") as file:
            for line in lines:
                components = line.split()

                # Change the class_id (first element) to the new class ID
                components[0] = str(new_class_id)

                # Write the updated annotation back to the file
                file.write(" ".join(components) + "\n")

print("Labels converted to a single label successfully.")
