import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)

#USE THIS CODE TO ACTIVATE VIRTUAL ENVIRONMENT:
#source venv/bin/activate


#SET FOLDER NAME FOR FRAMES
folder_frames_name = "Kab"


if not os.path.exists(f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames'):
    os.makedirs(f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames')

cap= cv2.VideoCapture(f"{dirname}/"+'Dance Videos/Kab.mp4')

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
        # save frame to zip and new video sample
        name = f"{dirname}/"+"Dance Frames/"+f'{folder_frames_name}_frames/' + str(count) + '.jpg'
        cv2.imwrite(name, img)












