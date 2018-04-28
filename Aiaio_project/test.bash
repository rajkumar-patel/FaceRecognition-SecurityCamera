#!/usr/bin/bash
#test.bash
#   Purpose:
#       Calls the label_image.py because it is a really long command
#       that we call several times
#       The image parameter is the picure that is tested against model,
#       this is passed as a command line argument 

python3 -m scripts.label_image --graph=tf_files/retrained_graph.pb --output_layer=final_result --image=$1

#this is originally what i had done
#I than realized, "Why am I using bash for this???"
#this code was placed in the label_image.py

#line=$(head -n 1 "outFile.txt")
#if [[ $line == "None" ]]; then
#    echo "*****NO MATCH FOUND, POSSIBLE INTRUDER*****"
#else
#    echo "*****MATCH FOUND, EMPLOYEE: $line*****"
#fi

