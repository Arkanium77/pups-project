import argparse
import os
from os.path import exists
from pathlib import Path
from shutil import copyfile as cp
from shutil import rmtree as rm


def flatter(catalog: str, clean: bool):
    count = 0
    for root, dirs, files in os.walk(catalog):
        if root == catalog: continue
        for f in files:
            copy_from = os.path.join(root, f)
            copy_to = os.path.join(catalog, f)
            n, x = os.path.splitext(f)
            i = 1
            while exists(copy_to):
                copy_to = os.path.join(catalog, f"{n}({i}){x}")
                i += 1
            cp(copy_from, copy_to)
            count += 1
    print(f"{count} files moved to root dir")
    if clean:
        for dir in os.listdir(catalog):
            dir_to_remove = os.path.join(catalog, dir)
            if Path(dir_to_remove).is_dir():
                rm(dir_to_remove)
        print(f"Redundant subdirs removed")
    print(f"Flatting of {catalog} complete!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This script for \"flatting\" of folders. It's extracts all files from "
                    "subfolders to the root directory, trying to avoid duplication",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--path", help="Path to the directory to \"flatten\" (default - current work dir)",
                        default=os.getcwd())
    parser.add_argument("-c", "--clean",
                        action='store_true',
                        help="Cleaning flag. If present - script will delete original files to avoid duplicating data")

    args = vars(parser.parse_args())
    path = args.get("path")
    clean = args.get("clean")
    flatter(path, clean)
