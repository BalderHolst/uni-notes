import re

def get_file_tags(path) ->  list:
    tags = []

    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")
        m = re.search(r"^#\w+", line)
        if m:
            for word in line.split(" "):
                tags.append(word[1:])
    return(tags)

if __name__ == "__main__":
    print(get_file_tags("/home/Balder/Documents/uni/noter/Gym/Halveringtid.md"))
