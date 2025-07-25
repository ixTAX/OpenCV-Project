import os
import cv2 as cv
import numpy as np

people = ['King Salman','King Abdullah','King Fahad']
DIR = r'C:\Users\Admin\Documents\GitHub\OpenCV-Project\OpenCV Face Recognition\Faces'

haar_cascade = cv.CascadeClassifier(r'C:\Users\Admin\Documents\GitHub\OpenCV-Project\OpenCV Face Recognition\haar_face.xml')

if haar_cascade.empty():
    raise IOError("Haar cascade xml file not loaded. Check the file path.")

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Warning: Failed to read image {img_path}")
                continue
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()

print("Training Done -------")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('faces_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)