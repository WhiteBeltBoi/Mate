#!/usr/bin/env python3
from pathlib import Path
import shutil

source_dir = Path("/Users/johndoe/Downloads")
text_destination = Path("/Users/johndoe/Documents/text_files")
picture_destination = Path("/Users/johndoe/Pictures/picture_collection")
counter = 0


for txt_file in source_dir.glob("*.txt"):
    shutil.move(str(txt_file), str(text_destination/txt_file.name))
    counter += 1

for pattern in ("*.jpg", "*.png","*.PNG", "*.HEIC","*.heic", "*.CR3", "JPEG"):
    for picture_file in source_dir.glob(pattern):
        shutil.move(str(picture_file), str(picture_destination/picture_file.name))
        counter += 1

print(f"Done, moved {counter} files")