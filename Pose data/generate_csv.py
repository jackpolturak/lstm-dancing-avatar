import mediapipe as mp
import cv2
import time
import numpy as np
import pandas as pd
import os
from sklearn.svm import SVC

dirname = os.path.dirname(__file__)



mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils # For drawing keypoints
points = mpPose.PoseLandmark # Landmarks
print(points)
path = f"{dirname}/"+"Dance Frames/Kab_frames" # enter dataset path

data = []
for p in points:
        x = str(p)[13:]
        data.append(x + "_x")
        data.append(x + "_y")
        data.append(x + "_z")
        # data.append(x + "_vis")
data = pd.DataFrame(columns = data) # Empty dataset


count_image = 1
count = 0

iteration_state = True

while iteration_state:

    for img in os.listdir(path):

        if img == f'{count_image}.jpg':

            print(img)
            count_image +=1

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

                        #temp = temp + [j.x, j.y, j.z, j.visibility]
                        temp = temp + [j.x, j.y, j.z]

                data.loc[count] = temp 

                count +=1

            cv2.imshow("Image", img)
            cv2.imshow("Blackie",blackie)
            cv2.waitKey(1)

            
            if count_image > len(os.listdir(path)):
                    iteration_state = False
                    break

        # else:
        #     print("No images to reference")




#Apply moving average filter WINDOW = 5 - May need to increase 
rolling = data.rolling(window=5)
main_df = rolling.mean()


#Save to csv
main_df.to_csv(f"{dirname}/"+'CSVs/Dance CSVs/Kab.csv', index=False) # save the data as a csv file no index



        

