'''''''''''''''''''''''''''''''''''''''''''''''''''
splitVideo.py
	Purpose: This is how we gathered our training 
	data. Each "Employee" takes a 30ish second video.
	This program goes throught the video and takes a 
	picture every frame. The pictures are placed in 
	a directory called data.
'''''''''''''''''''''''''''''''''''''''''''''''''''
import cv2
import os
import sys


if (len(sys.argv) != 2):
    print("Incorrect number of arguments")
    exit()

cap = cv2.VideoCapture(sys.argv[1])

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(currentFrame != 5000):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
