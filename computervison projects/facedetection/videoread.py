import cv2 as cv
capture = cv.VideoCapture('photos/videos/WhatsApp Video 2022-08-05 at 3.19.49 PM.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) % 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()