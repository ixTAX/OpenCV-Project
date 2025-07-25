# OpenCV-Project
### A project using OpenCV for recognizing the faces of Saudi Arabia Kings

### This project has a few steps
- Collecting the images of the people
- Training a model using these images via OpenCV
- Saving the model and the features/labels of the people
- Using the code "face_recognition.py" to run the model
- Using a sample pictures of these people for validation

### Collecting Images
I have collected 23 images for King Salman, 23 images for King Abdullah and 26 images for King Fahad

I wanted to do it for the previous kings as well but it is hard to find 20+ good images to use for the training

### Training a model and saving it
<img width="965" height="512" alt="image" src="https://github.com/user-attachments/assets/444a7533-5d72-49ed-8c5d-785ce931abc5" />

I trained the models using this code "faces_training.py" which train the model and save the features of the persons
and also connect it to the labels (their names)

The face recognition training for the Kings of Saudi Arabia is tricky since they all wear shemagh which covers

most of their faces and the shemagh might be added to the features of their faces

The model has been saved by the name "faces_trained.yml"

### Running the model
<img width="1154" height="414" alt="image" src="https://github.com/user-attachments/assets/e1bbcbd5-1766-4204-a4cc-f4c43479c417" />

This is the code used to run the model "face_recognition.py"

It uses the model "faces_trained.yml" on the picture in the path specefied on "img = cv.imread()"

And it draws a rectangle on the face if it is recognized and also write the name of the person + the confidence score

### Using sample pictures

<img width="1459" height="866" alt="Screenshot 2025-07-25 204843" src="https://github.com/user-attachments/assets/059eec35-6f0b-496d-865b-f7054b719d68" />

<img width="1427" height="947" alt="Screenshot 2025-07-25 205049" src="https://github.com/user-attachments/assets/fbcb1c42-36e1-4686-9280-70d65b6bf0e2" />

<img width="1574" height="886" alt="Screenshot 2025-07-25 205429" src="https://github.com/user-attachments/assets/4911f742-6364-4e54-9141-8e1d5c2461df" />

These are the picture I used to validate

In the first picture King Salman was recognized with a confidence score of 63%

In the second picture King Abdullah was recognized with a confidence score of 53%

In the third picture King Fahad was recognized with a confidence score of 71%

I conseder these good scores since they all wear shemagh

The images I used to train the model and to validate are included in the files
