# A0. Import dependencies 
import cv2
import mediapipe as mp 
import time 

# A1. Face Detection
##### A1.1 Read Video
cap = cv2.VideoCapture("Videos/clip.wmv")


# A2.1 
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

pTime = 0
while True:
    success, img = cap.read()

    # A2.1
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if(success):
        # cv2.waitKey(1)
        # A1.2 Display Frame Rate
        cv2.waitKey(1) # - Reduce Frame Rate by increasing the wait value, More wait time implies lesser frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
        cv2.imshow("Image",img)
    else:
        break;
