# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 612)
        MainWindow.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"  \n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 401, 611))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(239, 239, 239);\n"
"    border: none;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Camera_view = QtWidgets.QWidget(self.groupBox_2)
        self.Camera_view.setGeometry(QtCore.QRect(20, 20, 360, 360))
        self.Camera_view.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
"        border-radius: 180px;\n"
"}")
        self.Camera_view.setObjectName("Camera_view")
        self.Camera_border = QtWidgets.QLabel(self.groupBox_2)
        self.Camera_border.setGeometry(QtCore.QRect(20, 20, 361, 361))
        self.Camera_border.setStyleSheet("QLabel{\n"
"    background-color: none;\n"
"    border: 4px solid rgb(255, 255, 255);\n"
"    border-radius: 180px;\n"
"}")
        self.Camera_border.setText("")
        self.Camera_border.setObjectName("Camera_border")
        self.Face = QtWidgets.QLabel(self.groupBox_2)
        self.Face.setGeometry(QtCore.QRect(30, 430, 341, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.Face.setFont(font)
        self.Face.setStyleSheet("QLabel {\n"
"    background-color: none;\n"
"    border: none; \n"
"}")
        self.Face.setText("")
        self.Face.setAlignment(QtCore.Qt.AlignCenter)
        self.Face.setObjectName("Face")
        self.Copy_Right = QtWidgets.QLabel(self.groupBox_2)
        self.Copy_Right.setGeometry(QtCore.QRect(60, 580, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.Copy_Right.setFont(font)
        self.Copy_Right.setStyleSheet("QLabel {\n"
"    \n"
"    background-color: rgb(239, 239, 239);\n"
"}")
        self.Copy_Right.setObjectName("Copy_Right")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(160, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Minimun = QtWidgets.QPushButton(self.centralwidget)
        self.Minimun.setGeometry(QtCore.QRect(920, 20, 21, 21))
        self.Minimun.setStyleSheet("QPushButton#Minimun:hover:!pressed\n"
"{\n"
"      background-color: rgb(72, 72, 72);\n"
"}\n"
"QPushButton#Minimun {\n"
"    background-color: rgb(140, 140, 140);\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Minimun.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/minimum-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimun.setIcon(icon)
        self.Minimun.setObjectName("Minimun")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(950, 20, 21, 21))
        self.Close.setStyleSheet("QPushButton#Close:hover:!pressed\n"
"{\n"
"      background-color: rgb(167, 30, 30);\n"
"}\n"
"QPushButton#Close {\n"
"    background-color: rgb(220, 60, 60);\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/times-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close.setIcon(icon1)
        self.Close.setIconSize(QtCore.QSize(16, 16))
        self.Close.setObjectName("Close")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(420, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Version = QtWidgets.QLabel(self.centralwidget)
        self.Version.setGeometry(QtCore.QRect(940, 580, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.Version.setFont(font)
        self.Version.setObjectName("Version")
        self.ClassId = QtWidgets.QLabel(self.centralwidget)
        self.ClassId.setGeometry(QtCore.QRect(430, 310, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ClassId.setFont(font)
        self.ClassId.setStyleSheet("background:transparent;\n"
"border-radius:20px;\n"
"border : 2px solid;\n"
"border-top-color : black;\n"
"border-left-color :black;\n"
"border-right-color :black;\n"
"border-bottom-color : black;\n"
"color: orange;")
        self.ClassId.setText("")
        self.ClassId.setAlignment(QtCore.Qt.AlignCenter)
        self.ClassId.setObjectName("ClassId")
        self.NameStu = QtWidgets.QLabel(self.centralwidget)
        self.NameStu.setGeometry(QtCore.QRect(430, 170, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.NameStu.setFont(font)
        self.NameStu.setStyleSheet("background:transparent;\n"
"border-radius:20px;\n"
"border : 2px solid;\n"
"border-top-color : black;\n"
"border-left-color :black;\n"
"border-right-color :black;\n"
"border-bottom-color : black;\n"
"color: orange;\n"
"")
        self.NameStu.setText("")
        self.NameStu.setAlignment(QtCore.Qt.AlignCenter)
        self.NameStu.setObjectName("NameStu")
        self.Sex = QtWidgets.QLabel(self.centralwidget)
        self.Sex.setGeometry(QtCore.QRect(810, 170, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Sex.setFont(font)
        self.Sex.setStyleSheet("background:transparent;\n"
"border-radius:20px;\n"
"border : 2px solid;\n"
"border-top-color : black;\n"
"border-left-color :black;\n"
"border-right-color :black;\n"
"border-bottom-color : black;\n"
"color: orange;")
        self.Sex.setText("")
        self.Sex.setAlignment(QtCore.Qt.AlignCenter)
        self.Sex.setObjectName("Sex")
        self.ScoreStu = QtWidgets.QLabel(self.centralwidget)
        self.ScoreStu.setGeometry(QtCore.QRect(810, 310, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreStu.setFont(font)
        self.ScoreStu.setStyleSheet("background:transparent;\n"
"border-radius:20px;\n"
"border : 2px solid;\n"
"border-top-color : black;\n"
"border-left-color :black;\n"
"border-right-color :black;\n"
"border-bottom-color : black;\n"
"color: orange;")
        self.ScoreStu.setText("")
        self.ScoreStu.setAlignment(QtCore.Qt.AlignCenter)
        self.ScoreStu.setObjectName("ScoreStu")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(780, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:transparent;\n"
"\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 260, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:transparent;\n"
"\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 120, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:transparent;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Copy_Right.setText(_translate("MainWindow", "© dev by Badger Team X"))
        self.label.setText(_translate("MainWindow", "NAME"))
        self.label_2.setText(_translate("MainWindow", "📷 CAM"))
        self.Title.setText(_translate("MainWindow", "FACE RECONIZATION SYSTEMS"))
        self.Version.setText(_translate("MainWindow", "Ver 2.0.0"))
        self.label_3.setText(_translate("MainWindow", "📚 SCORE"))
        self.label_4.setText(_translate("MainWindow", "🤞 SEX"))
        self.label_5.setText(_translate("MainWindow", "📋 ID IN CLASS"))
        self.label_6.setText(_translate("MainWindow", "😊 FULL NAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
