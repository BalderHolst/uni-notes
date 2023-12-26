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
            info "Pulling $name's notes..."

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
    git clone "$url" "$path"
}

# Clone external's notes if the `--external` flag is provided
[[ "$1" = "--external" ]] && {

    # List of external vaults
    clone_external_vault "Kasper's Notes"         "https://github.com/TheJoboReal/Noter"
    clone_external_vault "Kasper's Formelsamling" "https://github.com/TheJoboReal/Formelsamling"
    clone_external_vault "Jacob's Notes"          "https://github.com/Jack-The-Dane/UNI_Notes"
    # clone_external_vault "LittleD3092's Notes"     "https://github.com/LittleD3092/My-Vault"

    done_something=1
}

if [[ $done_something = 1 ]]; then
    info "Done!"
else
    info "Nothing to do."
fi

