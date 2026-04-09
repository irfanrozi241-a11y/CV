import os

root = "/Users/irfan/Desktop/CV "
awards_path = os.path.join(root, "Awards")
editing_dir = [d for d in os.listdir(awards_path) if "Best Editing" in d][0]
full_path = os.path.join(awards_path, editing_dir)
files = os.listdir(full_path)

with open(os.path.join(root, "scratch/editing_files.txt"), "w") as f:
    f.write(editing_dir + "\n")
    for file in files:
        f.write(file + "\n")
