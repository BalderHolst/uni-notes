from get_file_tags import *

from pathlib import Path

gym_dir = Path("/home/Balder/Documents/uni/noter/Gym")

for file in gym_dir.iterdir():
    print(str(file))
