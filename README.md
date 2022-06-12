# lstm-dancing-avatar

Welcome to LSTM DANCING AVATAR! 

An intuative way to understand this code is go through the steps you would need to take to make your own dancing AI.

1. Record youself dancing (make sure NO ONE else is in the frame & that your camera is set to 30FPS).
2. Post edit some actual music into to the video (I used adobe premiere pro, but any old basic video editor will do). 
3. Export BOTH an mp3, and an mp4 of your boogie.
4. Nice! you've got everything you need to get crackalaking.

STEP 1 ==> Go to base folder "Pose Extract":
           1a. prepare_frames.py > This script "cuts" your video into all of it's individual frames, placing them in a folder.
           1b. generate_csv.py > This get's all of your joint positions for each frame and adds them to a csv dataframe.
   
STEP 2 ==> Go to base folder "Music Extract":
            2a. audio_features.py > This script extracts all low level audio features from ur mp3 export.
 
STEP 3 ==> Go BACK to base folder "Pose Extract": 
            3a. merge.py > combines all your dancing data to all the song data. Congrats! You've just generated a:
                           [synchronized dance motion and audio feature datasdet]. This is usually pretty expensive, you now owe me a coffee.
                       
STEP 4 ==> Go to base folder "Machine Learning":
            4a. network.py > This is where you train your puppet. But you will need to choose what model to use. I personallly like cnn_lstm()
                              But don't let me influence your choice. Dance is a subjective artform.
            4.b generate_dance.py > Does what it says on the tin, you will need to choose how long you want your puppet to dance for.

STEP 5 ==> DOWNLOAD BLENDER: https://www.blender.org     
            5a. Go to base folder "Visualize" > Copy and paste "visualize_csv.py" into the embedded python console
            5b. Run the script, it might take a while to generate.
            5c. Enjoy watching your AI puppet cut some shapes.
            
            
            
