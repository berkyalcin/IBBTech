import cv2
from PIL import Image
import numpy

UPPER_BOUND = 50
LOWER_BOUND = 0
IMAGE_CROP_X = (200,300)
IMAGE_CROP_Y = (0,300)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    npImage = numpy.asarray(grayImage)
    croppedImage = npImage[IMAGE_CROP_Y[0]:IMAGE_CROP_Y[1],IMAGE_CROP_X[0]:IMAGE_CROP_X[1]]

    mask = cv2.inRange(croppedImage,LOWER_BOUND,UPPER_BOUND)
    
    cv2.imshow("frame",mask)
    if cv2.waitKey(1) & (0xFF == ord('q')):
        break
