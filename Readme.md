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
### awake.py
This windows-only script is designed to keep the computer powered on without allowing it to go into hibernation mode. Unlike AWAKE from PowerToys or the simple power plans settings in windows, this "low-level" approach bypasses the corporate settings for automatically exit due to inactivity
- `-c`/`--count`: Count of key pressing/releasing actions.Default is 2 (i.e. key presses and then releases two times in a row).
- `-d`/`--delay`: The length of the delay between key pressing/releasing (in seconds). Default value is 0.001
- `-k`/`--key`: The code of the key used to perform the "awake" action. You can see the key codes here https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes (column "value"). Default value is 0x91 (SCROLLOCK)
- `-s`/`--silent`: Silent execution flag. If present - script will not write log of "awake" actions
- `-t`/`--timespan`: The length of the time span between "awake" actions (in seconds). Default value is 600 (10 minutes)
- `-ac`/`--awake_count`: Total count of awake actions. E.g. with --timespan=600 and --awake_count=6 script will awake your computer ~1 hour. Default value is 0 (Will working before manual interrupting e.g. Ctrl+C in terminal),