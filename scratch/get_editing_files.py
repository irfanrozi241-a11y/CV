import os

root_path = "/Users/irfan/Desktop/CV "
awards_path = os.path.join(root_path, "Awards")

# Find the folder
editing_folder = None
for entry in os.listdir(awards_path):
    if "Best Editing" in entry:
        editing_folder = entry
        break

if editing_folder:
    files = os.listdir(os.path.join(awards_path, editing_folder))
    with open(os.path.join(root_path, "scratch/editing_files.txt"), "w") as f:
        f.write(f"Folder: {editing_folder}\n")
        f.write("\n".join(files))
else:
    with open(os.path.join(root_path, "scratch/editing_files.txt"), "w") as f:
        f.write("FOLDER NOT FOUND")
