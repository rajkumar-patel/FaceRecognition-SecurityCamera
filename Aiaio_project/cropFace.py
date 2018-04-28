'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cropFace.py
	Purpose: Covnerts the screen shot image into a black and
		white cropped image containing just the face. It then 
		writes the new image to a directory holding all of the
		cropped images
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import warnings 
warnings.filterwarnings("ignore", category=FutureWarning)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cropScreenShot
	Purpose: Covnerts the screen shot image into a black and
		white cropped image containing just the face. It then 
		writes the new image to a directory holding all of the
		cropped images
	Parameters:
		screenShot - the name of the screen shot image
		i - for naming purposes, number of the screenShot
	Returns: returns the path name of the new cropped picture
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def cropScreenShot(screenShot, i):
    image = cv2.imread(screenShot)
	#This rotates the image because for some reason the screenshot
	#is always sideways
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, 270, 1.0)
    image = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Make a copy of the original image to draw face detections on
    image_copy = np.copy(image)

    # Convert the image to gray 
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces in the image using pre-trained face dectector
    faces = face_cascade.detectMultiScale(gray_image, 1.25, 6)

    if len(faces) > 0:
        print("********Face detected!********")
	
    if len(faces) == 0:
        print("********No face detected!********")
        return

    face_crop = []
    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 3)  
        face_crop.append(gray_image[y:y+h, x:x+w])

    for face in face_crop:
        cv2.imwrite("./cropDir/newpic" + str(i) + ".jpg", face)
        filename = "./cropDir/newpic" + str(i) + ".jpg"
        return filename

