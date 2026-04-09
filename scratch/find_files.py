import os

awards_path = "/Users/irfan/Desktop/CV /Awards"
for root, dirs, files in os.walk(awards_path):
    print(f"Path: {root}")
    for file in files:
        print(f"  File: {file}")
