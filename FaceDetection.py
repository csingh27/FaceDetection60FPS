# A0. Import dependencies 
import cv2
import mediapipe as mp 
import time 

# A1. Face Detection
##### A1.1 Read Video
cap = cv2.VideoCapture("Videos/1.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    # cv2.waitKey(10) - Reduce Frame Rate
