#!/bin/sh

dir=$(dirname $0)
dir_name="notes"

done_something=0

# if script is run by itself
[[ ! -d "$dir/.git" ]] && {
    git clone git@github.com:BalderHolst/uni-notes "$dir_name"
    dir="$dir/$dir_name"
    done_something=1
    echo "Cloned notes."
}

# if the repo exist
[[ -d "$dir/.git" ]] && [[ ! -d "$dir/.obsidian" ]] && {
    git clone git@github.com:BalderHolst/uni-notes-settings "$dir/.obsidian"
    git -C "$dir" update-index --assume-unchanged ".obsidian"
    done_something=1
    echo "Added settings."
}

# Function for cloning classmates's vaults
clone_classmate_vault ()
{
    [[ ! -d "$dir/" ]]
    name="$1"
    url="$2"
}

[[ "$1" = "--classmates" ]] && {
    
    done_something=1
}

[[ $done_something = 0 ]] && echo "Nothing to do."
