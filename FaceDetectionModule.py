import cv2
import mediapipe as mp 
import time 

class FaceDetector():
    def __init__(self, minDetectionCon= 0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils
        faceDetection = self.mpFaceDetection.FaceDetection(minDetectionCon)

    def findFaces(self,img,draw= True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []
        if results.detections:
            for id, detection in enumerate(results.detections):        
                mpDraw.draw_detection(img,detection)
                # A2.3 Draw detections manually 
                # C2.3 Why draw detections manually
                # C2.4 How detections are drawn manually
                bboxC = detection.location_data.relative_bounding_box
                # C2.5 Defining image shape
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append(img,bbox)
                cv2.putText(img, f'FPS: {int(detection.score[0]*100)}',
                        (bbox[0],bbox[1] - 20),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
        return img, bboxs

    def fancyDraw(self, img, bbox, l = 30, t = 7, rt = 1):
        x, y, w, h = bbox
        x1, y1 = x + q, y + h
        cv2.rectangle(img,bbox, (255,0,255),rt)
        cv2.line(img, (x,y),(x+1,y),(255,0,255),t)
        return img
    
def main():
    cap = cv2.VideoCapture("Videos/clip.wmv")
    pTime = 0 
    detector = FaceDetector()
    while True:    
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        cv2.waitKey(1)         
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(detection.score[0]*100)}', (bbox[0],bbox[1] - 20),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
        cv2.imshow("image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()


