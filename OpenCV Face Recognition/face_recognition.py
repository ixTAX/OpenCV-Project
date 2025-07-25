import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier(r'C:\Users\Admin\Documents\GitHub\OpenCV-Project\OpenCV Face Recognition\haar_face.xml')

if haar_cascade.empty():
    raise IOError("Haar cascade xml file not loaded. Check the file path.")

people = ['King Salman','King Abdullah','King Fahad']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("faces_trained.yml")

img = cv.imread(r'C:\Users\Admin\Documents\GitHub\OpenCV-Project\OpenCV Face Recognition\Faces\VKing Fahad\3205OB.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray) 

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
    
cv.imshow('The Detected Face', img)

cv.waitKey(0)