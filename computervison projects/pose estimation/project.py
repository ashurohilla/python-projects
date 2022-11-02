import cv2
import time
import poseModule as pm
import math
import serial
try:
    arduino = serial.Serial(port='COM15', baudrate=115200, timeout=.1)
except:
    print("port not found")
cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:
        x1, y1 = lmList[12][1], lmList[12][2]
        x2, y2 = lmList[20][1], lmList[20][2]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        length = math.hypot(x2 - x1, y2 - y1)
        print(length)
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)