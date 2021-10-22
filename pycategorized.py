"""
find all files with specific suffix and categorize them in type directory

"""



import  os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENT" : [".pdf", ".rtf", ".txt"],
    "AUDIO" : [".mp3"],
    "VIDEOS" : [".mov", ".avi", ".mp4"],
    "IMAGES" : [".jpg", ".jpeg", ".png"]
}


def pickdirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"



def organizedirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type = file_path.suffix.lower()
        directory = pickdirectory(file_type)
        directory_path = Path(directory)
        if directory_path.is_dir() != True:
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path))



