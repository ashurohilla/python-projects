import cv2 as cv

face_cascade = cv.CascadeClassifier('photos\harcascade_frontalface\haarcascade_frontalcatface.xml')
img = cv.imread('photos/frontal_face.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces: 
  cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv.imwrite("face_detected.png", img) 
print('Successfully saved')