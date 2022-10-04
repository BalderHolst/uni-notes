import re

def get_file_tags(path) ->  list:
    tags = []

    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        m = re.search(r"^#\w+", line)
        if m:
            print(line)

if __name__ == "__main__":
    get_file_tags("/home/Balder/Documents/uni/noter/Gym/Typer Psykologi.md")
