#!/bin/sh

dir=$(dirname $0)



# if the repo exist
[[ -d "$dir/.git" ]] && [[ ! -d "$dir/.obsidian" ]] && \
    git clone https://github.com/BalderHolst/uni-notes-settings "$dir/.obsidian" && \
    echo "Added settings." && exit 0

# if script is run by itself
[[ ! -d "$dir/.git" ]] && \
    git clone https://github.com/BalderHolst/uni-notes noter && \
    git clone https://github.com/BalderHolst/uni-notes-settings "$dir/.obsidian" && \
    echo "Cloned notes and added settings." && exit 0

echo "Nothing to do."
exit 0
