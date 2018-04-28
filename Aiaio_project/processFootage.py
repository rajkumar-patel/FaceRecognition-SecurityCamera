'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
processFootage.py
	Purpose:
		This is the driver function of the project. This
		opens the mp4 video, every 5 frames it caputers
		a screenshot and sends that image to cropScreenShot
		which returns a file name containing the cropped immage.
		Finally test.bash is called which calls label_image.py
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import cv2
import math
import subprocess
import time
from cropFace import cropScreenShot

videoFile = "securityFootage.mp4"
cap = cv2.VideoCapture(videoFile)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret != True):
        break
    if i % 5 == 0:
        filename = './screenshot.jpg'
        cv2.imwrite(filename, frame)
        newFile = cropScreenShot(filename, i)
        if newFile != None:
            print("*****CHECKING IMAGE: " + newFile + " *****")
            subprocess.call(["bash", "test.bash", newFile])
    i+=1
    #time.sleep(1) 
cap.release()
print ("Done!")
