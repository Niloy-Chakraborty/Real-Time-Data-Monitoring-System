import os, zipfile
from pyunpack import Archive
import pandas as pd
import pathlib
import glob

dir_name = 'E:\\HiWi_new\\example\\node0\\'#bytes_in\\'
dir_name_target= "E:\\HiWi_new\\data\\"
extension = ".7z"

os.chdir(dir_name) # change directory from working dir to dir with files
df = pd.DataFrame()
z=0
print(os.listdir(dir_name))
for item in os.listdir(dir_name): # loop through items in dir
    print(item)
    files= os.listdir(".\\"+item+"\\")
    path_final = dir_name_target + item + "\\"

    # create the same directory structure
    pathlib.Path(path_final).mkdir(parents=True, exist_ok=True)

    for i in files:
        path = os.path.abspath(item+"\\"+i)
        # extract all the zipped files into the new directory structure
        if path.endswith(extension): # check for extension
            Archive(path).extractall(path_final)






