import cv2 as cv
def rescale(frame , scale = 0.75):
    width = int ( frame.shape[1]*scale)
    height = int (frame.shape[0]*scale)
    dimensions = (width , height)  
    return cv.resize (frame, dimensions, interpolation = cv.INTER_AREA)
capture = cv.VideoCapture('C:/Users/rohil/Dropbox/PC/Desktop/opencv/photos/videos/WhatsApp Video 2022-08-05 at 3.19.49 PM.mp4')
def changeres(width, height):
    capture.set(width,height)
    capture.set(4,height)
while True:
    istrue, frame = capture.read()


    frame_resized = rescale(frame)
    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) % 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
