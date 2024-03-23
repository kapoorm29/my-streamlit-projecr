import cv2
import numpy as np   #1pixel = red green blue

cam = cv2.VideoCapture(0)  #0 is the default camera
while cam.isOpened():
    status, frame = cam.read()
    if not status:
        print('camera not available')
        break
    #logic implementation

    #display output
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break