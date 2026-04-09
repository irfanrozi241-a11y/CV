import os

root_path = "/Users/irfan/Desktop/CV "
awards_dirs = os.listdir(os.path.join(root_path, "Awards"))
for d in awards_dirs:
    if "Best Editing" in d:
        target = os.path.join(root_path, "Awards", d)
        print(f"Listing {target!r}")
        files = os.listdir(target)
        for f in files:
            print(f"  File: {f}")
