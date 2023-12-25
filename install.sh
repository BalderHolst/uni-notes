#!/bin/sh

dir=$(dirname $0)
dir_name="notes"

done_something=0

info () {
    echo -e "\u001b[36;1m""$@""\u001b[0m"
}

# if script is run by itself
[[ ! -d "$dir/.git" ]] && {
    info "Cloning notes..."
    git clone git@github.com:BalderHolst/uni-notes "$dir_name"
    dir="$dir/$dir_name"
    done_something=1
}

# if the repo exist
[[ -d "$dir/.git" ]] && [[ ! -d "$dir/.obsidian" ]] && {
    info "Adding settings..."
    git clone git@github.com:BalderHolst/uni-notes-settings "$dir/.obsidian"
    done_something=1
}

CLASSMATES_DIR="classmates"

# Function for cloning classmates's vaults
clone_classmate_vault ()
{
    name="$1"
    url="$2"
    path="$dir/$CLASSMATES_DIR/$name"

    [[ ! -d "$dir/$CLASSMATES_DIR" ]] && \
        mkdir "$dir/$CLASSMATES_DIR" && \
        info "Created '$CLASSMATES_DIR' directory."

    # Try to pull changes if the repo is already cloned
    [[ -d "$path" ]] && {
        if [[ -d "$path/.git" ]]; then
            info "Pulling $name's notes..."
            git -C "$path" pull
        else
            info "`$path` is not a git repo. Skipping..."
        fi
        return
    }
    info "Cloning $name's notes..."
    git clone "$url" "$path"
}

# Clone classmates's notes if the `--classmates` flag is provided
[[ "$1" = "--classmates" ]] && {
    clone_classmate_vault "Kasper" "https://github.com/TheJoboReal/Noter" & \
    clone_classmate_vault "Jacob" "https://github.com/Jack-The-Dane/UNI_Notes"
    sleep 0.5 # Wait for prints to happen as to not mess up prompt1
    done_something=1
}

if [[ $done_something = 1 ]]; then
    info "Done!"
else
    info "Nothing to do."
fi

