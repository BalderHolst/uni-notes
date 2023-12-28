# Notes for University
Notes for my robotics degree at University of Southern Denmark.

## Installation

The vault with settings can be installed using the install script. To download and run it use the command below.
```bash
curl https://raw.githubusercontent.com/BalderHolst/uni-notes/main/install.sh | bash
```
The install script can also be run after cloning the repo like this:
```bash
git clone https://github.com/BalderHolst/uni-notes notes
notes/install.sh
```

This is a simple script that clones this repo and installs my settings from the [settings repository](https://github.com/BalderHolst/uni-notes-settings). If you have already cloned this repo, you can also install settings automatically by running the `install.sh` script locally.

## External Vaults
To supplement my own notes i use a couple of other peoples vaults. These can be installed (cloned into the `External` directory) by providing the install script with the `--external` flag.
```bash
./install.sh --external
```
