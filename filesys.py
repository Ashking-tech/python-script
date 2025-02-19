import os
from pathlib import Path
import shutil
def move_files():
    os.chdir('/home/ash/python')
    Path("downloaded").mkdir(exist_ok=True)
    for files in os.listdir():
        if files in ['.git','.vscode','task tracker',"cool",'tasks.json', "downloaded"]:
           continue
    shutil.move(files, "downloaded")
    print(files)
move_files()
