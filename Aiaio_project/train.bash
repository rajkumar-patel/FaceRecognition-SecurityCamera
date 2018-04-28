#train.bash
#   Purpose:
#       This was placed in a bash script because the command is 
#       rediculously long. retrain.py is Google's code that uses the inception/mobileNet
#       pretrained model to add an additional layer.  
#   P.S.
#       The only parameters I messed with were the number of training steps, 
#       the model_dir, and the image_dir. For the model_dir I first used the mobilenet 
#       pretrained model. I then later changed it to inception for accuracy. And the 
#       image_dir is the directory holding all of the directories of pictures to be
#       trained on.

python3 -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files/inception --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/employees
