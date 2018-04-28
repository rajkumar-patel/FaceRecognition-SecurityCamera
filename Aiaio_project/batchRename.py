import os
import sys

directory = sys.argv[1]
filenames = os.listdir(directory)
i = 0
for file1 in filenames:
    string = directory + "/newImage" + str(i) + ".jpg"
    thisfile = directory + "/" + file1
    os.rename(thisfile, string)
    i += 1
