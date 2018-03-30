#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

# cap = cv2.VideoCapture(0)

has_detected = False
tracker = cv2.TrackerKCF_create()

haar_face_cascade = cv2.CascadeClassifier('./noPlate.xml')
cap = cv2.VideoCapture('http://192.168.5.165:8080/video')

while True:

    # Capture frame-by-frame

    (ret, frame) = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    # cv2.putText(gray, "Tracking failure detected", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # load cascade classifier training file for haarcascade

    cars = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=5)

    # print the number of faces found

    print ('Cars found: ', len(cars))

    # if len(cars)==1 and !has_detected:
    #     has_detected=True
    #     imwrite('./uploads/car.jpg')
    # elif len(cars)==0:
    #     has_detected=False

    if len(cars) == 1:
        for (x, y, w, h) in cars:
            bbox = (x, y, w, h)
            ok = tracker.init(gray, bbox)

            (ok, bbox) = tracker.update(gray)
            if ok:
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(
                    gray,
                    p1,
                    p2,
                    (255, 0, 0),
                    2,
                    1,
                    )


    

    # go over list of faces and draw them as rectangles on original colored

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame

    cv2.imshow('frame', gray)

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()
