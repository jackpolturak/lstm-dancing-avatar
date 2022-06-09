#WHEN EXTRACTING POSE SEQEUNCE - THIS IS THE FIRST SCRIPT TO BE RAN!
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)


#SET FOLDER NAME FOR FRAMES
folder_frames_name = "Kab_untrained_higher"

if not os.path.exists(f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames'):
    os.makedirs(f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames')

cap= cv2.VideoCapture(f"{dirname}/"+'Dance Videos/kab_untrained_higher.mp4')

#Ensure frame rate is 30 for consistent temporal density 
frame_rate= cap.get(cv2.CAP_PROP_FPS)
print('Frames per second : ', frame_rate,'FPS')
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('Number of frames: ', frame_count)

count = 0
while(count < frame_count):

    count +=1
    ret, frame = cap.read()
    if ret:
        print(count)
        img = frame
        # save frames
        name = f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames/' + str(count) + '.jpg'
        cv2.imwrite(name, img)












