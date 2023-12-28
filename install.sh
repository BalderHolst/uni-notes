#!/usr/bin/env bash

dir=$(dirname $0)
dir_name="notes"

done_something=0
private=0

info () {
    echo -e "\u001b[36;1m""$@""\u001b[0m"
}

[[ "$*" = *--private* ]] && {
    info "Private Mode: Using ssh for cloning vault."
    private=1
}

clone_private ()
{
    if [[ $private = 1 ]]; then
        git clone --depth 1 git@github.com:BalderHolst/$1 "$2"
    else
        git clone --depth 1 https://github.com/BalderHolst/$1 "$2"
    fi
}

# if script is run by itself
[[ ! -d "$dir/.git" ]] && {
    info "Cloning notes..."
    clone_private "uni-notes" "$dir_name"
    dir="$dir/$dir_name"
    done_something=1
}

# if the repo exist
[[ -d "$dir/.git" ]] && [[ ! -d "$dir/.obsidian" ]] && {
    info "Adding settings..."
    clone_private "uni-notes-settings" "$dir/.obsidian"
    done_something=1
}

EXTERNAL_DIR="External"

# Function for cloning external's vaults
clone_external_vault ()
{
    name="$1"
    url="$2"
    path="$dir/$EXTERNAL_DIR/$name"

    [[ ! -d "$dir/$EXTERNAL_DIR" ]] && \
        mkdir "$dir/$EXTERNAL_DIR" && \
        info "Created '$EXTERNAL_DIR' directory."

    # Try to pull changes if the repo is already cloned
    [[ -d "$path" ]] && {
        if [[ -d "$path/.git" ]]; then
            info "Pulling '$name'..."

            # Restore any changes that may have happened
            git -C "$path" restore .

            # Actualy pull the repo
            git -C "$path" pull

        else
            info "`$path` is not a git repo. Skipping..."
        fi
        return
    }
    info "Cloning repo '$name'..."
    git clone --depth 1 "$url" "$path"
}

# Clone external's notes if the `--external` flag is provided
[[ "$*" = *--external* ]] && {

    # List of external vaults
    clone_external_vault "Kasper's Notes"         "https://github.com/TheJoboReal/Noter"
    clone_external_vault "Kasper's Formelsamling" "https://github.com/TheJoboReal/Formelsamling"
    clone_external_vault "Jacob's Notes"          "https://github.com/Jack-The-Dane/UNI_Notes"

    done_something=1
}

if [[ $done_something = 1 ]]; then
    info "Done!"
else
    info "Nothing to do."
fi

