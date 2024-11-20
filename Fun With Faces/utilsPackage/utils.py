# utils.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import os

def load_jpg_file_names(directory):
    """
    Reads all .jpg file names in the specified directory.
    @param directory str: The file directory to search
    @return list: The files that end in .jpg in the directory. 
    """
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            files.append(directory + filename)
            #print(filename)
    return files
