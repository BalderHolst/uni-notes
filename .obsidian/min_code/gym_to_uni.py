from get_file_tags import *

from pathlib import Path

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

tags = []

for file in gym_dir.iterdir():
    if file.is_file():
        pass

        # if ""


