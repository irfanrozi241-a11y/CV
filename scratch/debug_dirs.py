import os

awards_path = "/Users/irfan/Desktop/CV /Awards"
for entry in os.listdir(awards_path):
    print(f"Name: {entry!r}, Bytes: {entry.encode()!r}")
