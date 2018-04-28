'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#cropDir.py
#	Purpose: This was used for cleaning the data. After 
#		several attempts of getting bad training results, we
#		decided to clean our data by cropping out the face 
#		and grayscaling it. It loops throught the directory 
#		of images and creates a new directory of cropped 
#		images.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

dataDir = sys.argv[1]
if not os.path.exists(dataDir):
    print('Directory does not exist')
    sys.exit()
newDir = "./newDir/"
#try:
#    os.makedirs(newDir)
#except:
#    print("Creating new directory failed")
#    sys.exit()
i = 0
for picture in os.listdir(dataDir):
    picture = dataDir + "/" + picture
    filename = "" + newDir + "image" + str(i) + ".jpg"
    image = cv2.imread(picture)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_copy = np.copy(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, 1.25, 6)
    if len(faces) == 0:
        continue
    face_crop = []
    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 3)
        face_crop.append(gray_image[y:y+h, x:x+w])

    for face in face_crop:
        cv2.imshow('face',face)
        cv2.imwrite(filename, face)


    i += 1
