#!/bin/sh

dir=$(dirname $0)

dir_name="notes"

# if the repo exist
[[ -d "$dir/.git" ]] && [[ ! -d "$dir/.obsidian" ]] && {
    git clone git@github.com:BalderHolst/uni-notes-settings "$dir/.obsidian"
    git -C "$dir" update-index --assume-unchanged ".obsidian"
    echo "Added settings."
    exit 0
}

# if script is run by itself
[[ ! -d "$dir/.git" ]] && {
    git clone git@github.com:BalderHolst/uni-notes "$dir_name"
    git clone git@github.com:BalderHolst/uni-notes-settings "$dir/$dir_name/.obsidian"
    git -C "$dir/$dir_name" update-index --assume-unchanged ".obsidian"
    echo "Cloned notes and added settings."
    exit 0
}

echo "Nothing to do."
exit 0
