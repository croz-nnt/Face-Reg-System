import os
import random
import sys
import threading
import webbrowser

from PyQt5.QtCore import QUrl, QTimer, Qt
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QImage, QBrush, QPalette
from user_interface import Ui_MainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QLabel, QMainWindow, QPushButton

import queue
from collections import deque
import cv2, os, csv, time
import numpy as np
# import pyrebase
import pandas as pd

# firebaseConfig = {
#     "apiKey": "AIzaSyDw1662Yi3M7bIbo7l9WSskWSJ_DAVdQeg",
#     "authDomain": "facedetectdap.firebaseapp.com",
#     "databaseURL": "https://facedetectdap-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "facedetectdap",
#     "storageBucket": "facedetectdap.appspot.com",
#     "messagingSenderId": "543154448794",
#     "appId": "1:543154448794:web:5229abf4ceb4c2efe03223",
#     "measurementId": "G-P3YCC69F2G"
# }
#
# firebase = pyrebase.initialize_app(firebaseConfig)


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('models/trainer.yml')
face_cascade_Path = "models/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(face_cascade_Path)
font = cv2.FONT_HERSHEY_SIMPLEX
database_path = "D:/PYTHON/TrucCode/real-time-face-recognition/app/database/database.csv"
data = pd.read_csv(database_path)
id = 0
# names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
names = ['None','Truc','Phuoc','Loc'] # add a name into this list



ROOT_DIR = os.path.abspath(os.curdir)
ICON_PATH = os.path.join(ROOT_DIR, 'images/logo.png')

running = False
q = queue.Queue()
pts = deque(maxlen=64)

def send_data(name,id_class, sex,score, id):
    db = firebase.database()
    data = {'name':str(name),
            'id_class':str(id_class),
            'sex':str(sex),
            'score':str(score)
            }
    code_id = 'student_'+ str(id)
    db.child("class").child(code_id).set(data)
    return 0

def grab(cam, que, width, height, fps):
    global id
    global running
    capture = cv2.VideoCapture(cam)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    capture.set(cv2.CAP_PROP_FPS, fps)
    while running:
        frame = {}
        capture.grab()
        retval, img = capture.retrieve(0)
        frame["img"] = img
        if que.qsize() < 1:
            que.put(frame)

class CameraView(QWidget):
    def __init__(self, parent=None):
        super(CameraView, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        img_size = image.size()
        self.setMinimumSize(img_size)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        if self.image:
            qp.setPen(Qt.NoPen)
            brush = QBrush(self.image)
            qp.setBrush(brush)
            qp.drawEllipse(0, 0, 360, 360)
        qp.end()


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.screen1_w = self.ui.Camera_view.frameSize().width()
        self.screen1_h = self.ui.Camera_view.frameSize().height()
        self.ui.Camera_view = CameraView(self.ui.Camera_view)
        self.timer = QTimer(self)

        self.close = self.ui.Close.clicked.connect(self.salir)
        self.timer.timeout.connect(self.update)
        self.timer.timeout.connect(self.get_name)
        # self.name = self.ui.Face.setText(self.get_name)
        self.timer.start(10)
        self.n = 0

        global running

        running = True
        capture_thread.start()



    def update(self):
        if not q.empty():
            frame = q.get()
            img = frame["img"]
            img_height, img_width, img_colors = img.shape
            scale = self.screen1_h / img_height
            looking = ['LOOK_R', 'LOOK_L']
            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            height, width, bpc = img.shape
            bpl = 3 * width
            wd01 = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.ui.Camera_view.setImage(wd01)



    def get_name(self):
        if not q.empty():
            frame = q.get()
            img = frame["img"]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(64, 48),
            )
            for (x, y, w, h) in faces:
                # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                if (confidence < 100):
                    id = id - 1
                    name = str(data.loc[id]['name'])
                    full_name = str(data.loc[id]['full_name'])
                    id_class = str(data.loc[id]['id_class'])
                    sex = str(data.loc[id]['sex'])
                    score = str(data.loc[id]['score'])
                    self.ui.NameStu.setText(full_name)
                    self.ui.ClassId.setText(id_class)
                    self.ui.Sex.setText(sex)
                    self.ui.ScoreStu.setText(score)
                    self.ui.Face.setText(name)
                    # send_data(full_name, id_class, sex, score, id + 1)



                else:
                    # Unknown Face
                    id = None
                    # confidence = "  {0}%".format(round(100 - confidence))





    def salir(self):
        self.close()
capture_thread = threading.Thread(target=grab, args=(0, q, 720, 1280, 60))

app = QApplication(sys.argv)
w = MyWindow(None)
w.windowTitle()
w.show()
app.exec_()
sys.exit(app.exec())

