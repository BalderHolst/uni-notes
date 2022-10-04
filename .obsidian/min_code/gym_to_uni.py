from get_file_tags import *

from pathlib import Path
import shutil

# TAGS
# =================
# historie
# old
# personer
# psykologi
# matematik <-
# religion
# dansk
# retorik
# fysik <-
# tekst
# funktioner
# todo
# idræt
# avis
# test
# gud
# samfundskab
# tidslinje
# kemi
# filosofi
# samfundsfag
# informatik

notes_dir = Path("/home/Balder/Documents/uni/noter")
gym_dir = notes_dir / Path("Gym")
dst_dir = notes_dir / "unmarked"

for file in gym_dir.iterdir():
    if file.is_file():
        file_tags = get_file_tags(file)
        if len(file_tags) == 0:
            tag = input(f"{file.name!r} - Assign tag (enter to skip): ")

            if tag != "":
                with file.open() as f:
                    lines = f.readlines()
                lines.append("---\n")
                lines.append(f"#{tag}\n")

                with open(dst_dir / file.name, 'w') as f:
                    f.writelines(lines)



# # Move fysik og matematik
# for file in gym_dir.iterdir():
#     if file.is_file():
#         file_tags = get_file_tags(file)
#         if "matematik" in file_tags or "fysik" in file_tags:
#             new_path = notes_dir / file.name
#             if new_path.exists():
#                 print(f"{new_path!r} exists!")
#                 quit()
#             shutil.move(file, new_path) 
#             print(f"moved {file!r} -> {new_path!r}")
            


