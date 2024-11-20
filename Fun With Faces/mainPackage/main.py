# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# Fun With OpenCV
# https://opencv.org/get-started/

import cv2
import numpy as np
from openCVPackage.fun_with_faces import *
from utilsPackage.utils import *
   
if __name__ == "__main__":
    """
    fun_with_faces.face_fun("Images/Crowd/Crowd.jpg",
                            ["Images/Crowd/random person in crowd1.jpg", 
                             "Images/Crowd/random person in crowd.jpg"
                            ]) 
    """
    group_photo = "us.jpg"
    directory = "Images/Us/"
    files = load_jpg_file_names(directory)
    try:
        files.remove(directory + group_photo)    
    except:
        pass

    print("files that will be searched:", files)
    fun_with_faces.face_fun("Images/Us/us.jpg", files, label_unknowns = True, verbose = True)
