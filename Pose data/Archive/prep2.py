import mediapipe as mp
import cv2
import time
import numpy as np
import pandas as pd
import os
from sklearn.svm import SVC


cap = cv2.VideoCapture('/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/Dance Videos/HANDUP[.mov')


current_frame = 0

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print(frame_count)

while(current_frame < frame_count):
    ret, frames = cap.read()
    if ret:
        name = f'/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/frames/{current_frame}.jpg'
        cv2.imwrite(name, frames)
        current_frame += 1
    #print(current_frame)

cv2.destroyAllWindows()