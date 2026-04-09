import os
import glob

root = "/Users/irfan/Desktop/CV "
search_pattern = os.path.join(root, "Awards", "Best Editing*")
matches = glob.glob(search_pattern)

if matches:
    target = matches[0]
    files = os.listdir(target)
    with open(os.path.join(root, "editing_files.txt"), "w") as f:
        f.write(f"Target: {target}\n")
        for file in files:
            f.write(file + "\n")
else:
    with open(os.path.join(root, "editing_files.txt"), "w") as f:
        f.write("No matches found\n")
