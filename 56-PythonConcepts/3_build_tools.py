from pathlib import Path

def rename_jpegs(folder: str):
    for file in Path(folder).glob("*.jpeg"): # Finds all files ending with .jpeg in the specified folder
        file.rename(file.with_suffix(".jpg")) # Rename to .jpg