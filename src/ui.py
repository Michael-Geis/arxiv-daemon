import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window


def search_for_file_path(prompt="Please select a directory"):
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title=prompt)
    if not len(tempdir) > 0:
        print("It's FUCKED.")
    return tempdir
