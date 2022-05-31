import mediapipe as mp
import cv2
import time
import numpy as np
import pandas as pd
import os
from sklearn.svm import SVC

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils # For drawing keypoints
points = mpPose.PoseLandmark # Landmarks
print(points)
path = "/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/frames" # enter dataset path

data = []
for p in points:
        x = str(p)[13:]
        data.append(x + "_x")
        data.append(x + "_y")
        # data.append(x + "_z")
        # data.append(x + "_vis")
data = pd.DataFrame(columns = data) # Empty dataset


count = 0

for img in os.listdir(path):


        temp = []

        img = cv2.imread(path + "/" + img)

        imageWidth, imageHeight = img.shape[:2]

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        blackie = np.zeros(img.shape) # Blank image

        results = pose.process(imgRGB)

        if results.pose_world_landmarks:

                mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) #draw landmarks on image

                mpDraw.draw_landmarks(blackie, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # draw landmarks on blackie

                landmarks = results.pose_world_landmarks.landmark

                for i,j in zip(points,landmarks):
                        

                        # temp = temp + [j.x, j.y, j.z, j.visibility]
                        temp = temp + [j.x, j.y]
   

                data.loc[count] = temp 

                
                count +=1
                print(count)
        
        # print(data)

        cv2.imshow("Image", img)

        cv2.imshow("blackie",blackie)

        cv2.waitKey(400)

data.to_csv('/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Pose data/CSVs/data.csv') # save the data as a csv file
