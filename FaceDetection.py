# A0. Import dependencies 
# Concept C0.1 - What is OpenCV Library
# Concept C0.2 - What is MediaPipe Library
# Concept C0.3 - What is Time Library
# C0.1 - 
# C0.2 - MediaPipe Library is provided by Google 
# C0.3 - Time library is used to display the frame rate
import cv2
import mediapipe as mp 
import time 

# A1. Display Video
##### A1.1 Read Video
cap = cv2.VideoCapture("Videos/clip.wmv")

# A2.1  Face Detection
# C2.1 - Face Detection using Media Pipe
# C2.2 - Media Pipe Drawing Ability
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()
# A2.4 - Minimum detection confidence
# C2.4 - Minimum detection confidence

pTime = 0
while True:    
    success, img = cap.read()
    if(success):
        
        # A2.1 Face Detection
        # C2.1 - RGB Image CV
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # A2.2 Frame Rate reduction when Face Detection is being processed 
        results = faceDetection.process(imgRGB)
        print(results)

        # A2 Visualize detections 
        if results.detections:
            for id, detection in enumerate(results.detections):
                
                # A2.1 Print detections 
                # print(id, detection)
                # print(detection.score)
                # print(detection.location_date.relative_bounding_box)
                
                # A2.2 Display detections using mpDraw
                # C2.2 mpDraw draw_detections
                
                mpDraw.draw_detection(img,detection)
                # A2.3 Draw detections manually 
                # C2.3 Why draw detections manually
                # C2.4 How detections are drawn manually
                bboxC = detection.location_data.relative_bounding_box
                # C2.5 Defining image shape
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img,bbox, (255,0,255),2)
                cv2.putText(img, f'FPS: {int(detection.score[0]*100)}',
                        (bbox[0],bbox[1] - 20),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
            # cv2.waitKey(1)
            # A1.2 Display Frame Rate
            cv2.waitKey(1) # - Reduce Frame Rate by increasing the wait value, More wait time implies lesser frame rate
            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            # concept C1.1 : 
            # concept C1.2 - f-stringes : https://www.youtube.com/watch?v=o0mvgsPQ8Jg
            # Concept C1.3 - cv2.putText function
            # Concept C1.4 - 
            # C1.3 : (20,70) = FPS, Font, Scale = 3, colour (0,255,0), thickness = 2
            # C1.4 : cv2.imshow()
            # Position of displaying FPS 
            cv2.putText(img, f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
            cv2.imshow("Image",img)
        else:
            break;
