import cv2 as cv
face_cascade = cv.CascadeClassifier("photos\harcascade_frontalface\haarcascade_frontalface_default.xml")

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x, y, w, h) in faces: 
         cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame


Capture = cv.VideoCapture(0)

#this function do a while loop iteration for camera
while True:
    _, frame = Capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv.imshow('video', canvas )
    if cv.waitKey(20) % 0xFF == ord('d'):
        break
cv.destroyAllWindows()    
Capture.release()


