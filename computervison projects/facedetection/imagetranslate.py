from turtle import width
import numpy as np
import cv2 as cv
image = cv.imread('photos/download.jfif')
cv.imshow('image', image)
def translate(image,x,y):
    transmat =  np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image,transmat,dimensions)
trasnlate = translate(image, 50, 50)
#cv.imshow('translate',trasnlate)

# rotation
def rotate(image, angel,rotPoint= None):
    (height,width) = image.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angel,1.0)
    dimension = (width,height)
    return cv.warpAffine( image,rotMat,dimension)
rotated = rotate(image, -45)
cv.imshow('image', rotated)    


cv.waitKey(0)