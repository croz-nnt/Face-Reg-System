import cv2, os, csv, time
import numpy as np
import pyrebase
import pandas as pd


firebaseConfig = {
  "apiKey": "AIzaSyCCA7vixEir-HLexU4cHzDgfpnUpUtwly4",
  "authDomain": "truccodeidentifyface.firebaseapp.com",
  "databaseURL": "https://truccodeidentifyface-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "truccodeidentifyface",
  "storageBucket": "truccodeidentifyface.appspot.com",
  "messagingSenderId": "319431023142",
  "appId": "1:319431023142:web:5037003c2df05102d064e7",
  "measurementId": "G-8CGYSDGW3V" }

firebase = pyrebase.initialize_app(firebaseConfig)
def send_data(name,id_class, sex,score, id):
    db = firebase.database()
    data = {'name':str(name),
            'id_class':str(id_class),
            'sex':str(sex),
            'score':str(score)
            }
    code_id = 'student_'+ str(id)
    db.child("class").child(code_id).set(data)
    return print(" %% present %% ")
database_path = 'app/database/database.csv'
data = pd.read_csv(database_path)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('models/trainer.yml')

face_cascade_Path = "models/haarcascade_frontalface_default.xml"


faceCascade = cv2.CascadeClassifier(face_cascade_Path)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
# names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
names = ['None','Truc','Phuoc','Loc'] # add a name into this list
#Video Capture
cam = cv2.VideoCapture(-1)
cam.set(3, 640)
cam.set(4, 480)
# Min Height and Width for the  window size to be recognized as a face
print(cam.get(3))
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
print(minW,minH)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        with open('diemdanh.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'diemdanh'])
            if (confidence < 100):
                id = id - 1
                name = data.loc[id]['name']
                id_class = data.loc[id]['id_class']
                sex = data.loc[id]['sex']
                score = data.loc[id]['score']
                send_data(name,id_class,sex,score,id + 1)

            else:
                # Unknown Face
                id = "Who are you ?"
                confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)
    # Escape to exit the webcam / program
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
print("\n [INFO] Exiting Program.")
cam.release()
cv2.destroyAllWindows()
