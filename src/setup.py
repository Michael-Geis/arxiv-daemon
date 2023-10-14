import tkinter
from tkinter import filedialog
import os
import subprocess
import time

root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window


def search_for_file_path(prompt="Please select a directory"):
    userdir = os.environ.get("USERPROFILE")
    tempdir = filedialog.askdirectory(parent=root, initialdir=userdir, title=prompt)
    if not len(tempdir) > 0:
        return None
    return tempdir


def main():
    source_dir = search_for_file_path(prompt="Select your downloads directory.")
    time.sleep(1)
    target_dir = search_for_file_path(
        prompt="Select the directory you want your papers to be saved in."
    )
    if os.name == "nt":  # if is in windows
        exp_source = f'setx DOWNLOADS "{source_dir}"'
        exp_target = f'setx PAPERS "{target_dir}"'
        if source_dir:
            subprocess.Popen(exp_source, shell=True).wait()
        else:
            print("Source directory not set, re-run setup.bat before continuing")
        if target_dir:
            subprocess.Popen(exp_target, shell=True).wait()
        else:
            print("Target directory not set, re-run setup.bat before continuing.")


if __name__ == "__main__":
    main()
