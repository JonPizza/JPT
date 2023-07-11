import cv2, sys, settings

if len(sys.argv) > 1:
    vid = cv2.VideoCapture(int(sys.argv[1]))
else:
    vid = cv2.VideoCapture(settings.CAMERA_ID)

while vid.isOpened():
    res, frame = vid.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

