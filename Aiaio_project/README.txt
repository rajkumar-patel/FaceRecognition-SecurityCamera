Aiaio_project/
    
    cropDir - the directory that holds all of the cropped images from the security footage,
        after running the program, delete the contents of this folder.
    
    scripts - directory of the python files from Google's tensorflow codelabs. I REPEAT, **Aiaio DID NOT WRITE/OWN
        ANY OF THE FILES IN THIS DIRECTORY**. I did however change the label_image.py to better suit my needs.
    
    tf_files - directory that holds our gathered gathered data, and some output from retrain.py
        employees - holds the pictures of our cropped faces for training, originally there was a total of 7 
        employees with a thousand images each but for accuracy purposes it was shortened to 3.
    
    cropDir.py - team Aiaio is the author of this program, used to clean the data
    
    cropFace.py - team Aiaio is the author of this program, used to crop a face from a single image
    
    haarcascade_frontalface_default.xml - this is used by crop face to detect faces
    
    processFootage.py - team Aiaio is the author of this program, the driver program 
    
    securityFootage.mp4 - video to test our program, the goal is to recognize the first and second person, not the third person
    
    splitVideo.py - team Aiaio is the author of this program, used to collect data, creates N number of images from video
    
    batchRename.py - team Aiaio is the author of this program, used this to rename a huge directory of files 

    test.bash - calls label_image.py 
    
    train.bash - calls retrain.py

How to Run:
    python3 processFootage.py
    *For your viewing pleasure, open the cropDir, after running the above line, to see the current picture it is evaluating

Versions needed:
    python3 3.4.3 
    tensorflow 1.7.0 
    numpy 1.14.2
    cv2 3.4.0
    matplotlib 2.2.2

What does not work?
    Everything works for the most part but the results are sometimes random. The algorithm
    tends to favor Raj as you will see in the results. Also we did not meet all of our goals. 
    We wanted a green box to track recognized faces and a red box for intruders. 
    We also wanted to use more pictures and more employees, however, more employees made our results more inaccurate. 

