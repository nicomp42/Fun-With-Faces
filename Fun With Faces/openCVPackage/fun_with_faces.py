# fun_with_faces.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# Use the face_recognition package to find and identify faces
# OpenCV is used a little, but just to manipulate and display the image, not to deal with face-finding
# ****************************************************************************************
# To get the face_recognition package to install and function properly:
# 1. Select the active environment
# 2. Open Powershell from the VS Envirionment manager and enter:
# pip install cmake==3.25.2
# pip install dlib==19.24.2
# pip install face_recognition
# Now we downgrade numpy so face_recognition.face_locations in FaceFun.py will work
# pip uninstall numpy
# pip install numpy==1.26.0
# ****************************************************************************************

import cv2
import face_recognition
from PIL import Image

class fun_with_faces:
    
    def face_fun(target_image_file, image_file_known_persons, label_unknowns = True, unknown_label = "unknown", verbose = False):
        """
        Search for a face against a set of sample faces. Displays the target image with faces identified and labeled. 
        @param target_image_file str: The path to the jpeg containing the file to be identified
        @param image_file_known_persons list[str]: A list of file paths to search for in the target_image_file image
        @param label_unknowns bool: if true, all faces that wer found in image_file will be outlined and labeled with the contents of unknown_label. Defaults to True
        @param unknown_label str: The label to use on faces that could not be identified. Defaults to "unknown"
        @param verbose Boolean: If True, print commentary while processing. Defaults to False
        """
        print("fun_with_faces.face_fun()...")
        match_count = 0
        # Load the image to identify
        image = face_recognition.load_image_file(target_image_file)

        # Find all the faces in the image, then compute those face encodings
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)  

        # Load the known face images and their encodings
        known_images = []
        known_face_encodings = []
        for image_file_known_person in image_file_known_persons:
            if verbose: print("  Processing known image", image_file_known_person)
            known_image = face_recognition.load_image_file(image_file_known_person)
            known_images.append(known_image)
            try:
                known_face_encoding = face_recognition.face_encodings(known_image)[0]  
                known_face_encodings.append([known_face_encoding, image_file_known_person])
                if verbose: print(" Found a face in it")
            except Exception as ex:
                # No face was found in the known image, for whatever reason
                #pass
                print("Exception while processing", image_file_known_person)
                print(ex)
        # Compare the faces in the image to the known face
        if verbose: print(" Comparing the faces in the group photo to the known image...")       
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            match_found = False
            for known_face_encoding in known_face_encodings:
                matches = face_recognition.compare_faces([known_face_encoding[0]], face_encoding)
                name = unknown_label
                try:
                    if matches[0]:
                        match_count += 1
                        #name = "Known Person"
                        #name = known_face_encoding[1].split("/")[-1]
                        name = known_face_encoding[1].split("/")[-1].split(".")[0]
                        if verbose: print("  Found a match for", known_face_encoding[1].split("/")[-1], "in the group photo")
                        # Draw a box around the face and label it
                        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                        cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
                        match_found = True
                        break   # We found a match. Stop trying.
        
                except Exception as ex:
                    #pass
                    print("Exception:", ex)
            
            if not match_found:
                if label_unknowns:
                    name = unknown_label
                    # Draw a box around the face and label it
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
                
        if verbose: print(match_count, "photo matches found")
        
        # Display the image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()