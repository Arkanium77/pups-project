# Personal Use Python Scripts
## About repo
Some useful python scripts. Written for personal use, but if you need them - just take them.
### Rules
- One functionality = one file
- No dependencies, just the standard library
- A script can have args, but MUST be able to run without them. Double-click on file and it's done
## Script catalog
### folderflatter.py
This script for "flatting" of folders. It's extracts all files from subfolders to the root directory, trying to avoid duplication
Path to the directory to "flatten" (default - current work dir.
It's applies to params
- `-p`/`--path`: Path to the root of flattable directory (default - current work dir)
- `-c`/`--clean`: Cleaning flag. If present - script will delete original files to avoid duplicating data 