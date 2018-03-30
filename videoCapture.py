import numpy as np
import cv2
import requests
import json

# cap = cv2.VideoCapture(0)

has_detected=False
owner_name=''

haar_face_cascade = cv2.CascadeClassifier('./noPlate.xml')
cap = cv2.VideoCapture('http://172.20.10.3:8080/video')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    gray = frame

    

    #load cascade classifier training file for haarcascade 

    cars = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5);  
     
    #print the number of faces found 
    print('Cars found: ', len(cars))

    if len(cars)!=0 and not has_detected:
        has_detected=True
        cv2.imwrite('./uploads/car.jpg', gray)

        # owner=requests.get("http://127.0.0.1:5000/owner/https://98038321.ngrok.io/get_image/car.jpg")

        # data=json.loads(owner.text)

        # owner_name=data['rcServiceResponse']['veh_dts']['owner_name']

        # print(owner_name)

        # cv2.putText(frame, "Owner : "+owner_name , (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    else:
        # cv2.putText(frame, "Owner : "+owner_name , (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        pass
        # has_detected=False

    # if len(cars)==1:
    #     bbox = (287, 23, 86, 320)

    #go over list of faces and draw them as rectangles on original colored 
    for (x, y, w, h) in cars:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

	# Display the resulting frame
    cv2.imshow('frame', gray)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()