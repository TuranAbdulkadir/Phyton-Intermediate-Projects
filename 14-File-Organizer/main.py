import os
import shutil

# Organize current directory
dirs = {
    "IMAGES": [".jpg", ".png", ".jpeg"],
    "DOCS": [".pdf", ".txt", ".docx"],
    "AUDIO": [".mp3", ".wav"]
}

for file in os.listdir():
    name, ext = os.path.splitext(file)
    for folder, extensions in dirs.items():
        if ext.lower() in extensions:
            if not os.path.exists(folder): os.makedirs(folder)
            shutil.move(file, f"{folder}/{file}")
            print(f"Moved {file} to {folder}")