import os

import sys
sys.path.insert(0, os.path.dirname(__file__).replace("GUI", "Models"))
from predict import predict_img

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PredictionScreen import Ui_PredictionWindow


ui_path = os.path.join(os.path.dirname(__file__), "MainScreen.ui")
desktop_path = os.path.expanduser("~/Desktop")


class Ui_MainScreen(QWidget):

    file_path = ""

    def openPredictionWindow(self):

        self.window2 = QtWidgets.QDialog()
        self.ui = Ui_PredictionWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
        MainScreen.hide()

        prediction = predict_img(self.file_path)
        self.ui.Prediction.setText("Your image is a " + prediction + "!")
        self.ui.Image.setPixmap(QPixmap(self.file_path))
        
     
    def browsefiles(self):

        filter_type = "Images (*.png *.xpm *.jpg *.jfif)"

        filename = QFileDialog.getOpenFileName(self, "File Explorer", desktop_path, filter=filter_type)
        self.file_path = filename[0]
        self.Filepath.setText(self.file_path)


    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(641, 488)
        self.label = QtWidgets.QLabel(MainScreen)
        self.label.setGeometry(QtCore.QRect(70, -20, 521, 141))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Browse = QtWidgets.QPushButton(MainScreen, clicked= lambda: self.browsefiles())
        self.Browse.setGeometry(QtCore.QRect(480, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Browse.setFont(font)
        self.Browse.setObjectName("Browse")
        self.Filepath = QtWidgets.QLineEdit(MainScreen)
        self.Filepath.setGeometry(QtCore.QRect(40, 300, 411, 31))
        self.Filepath.setObjectName("Filepath")
        self.Ok = QtWidgets.QPushButton(MainScreen, clicked= lambda: self.openPredictionWindow())
        self.Ok.setGeometry(QtCore.QRect(210, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Ok.setFont(font)
        self.Ok.setObjectName("Ok")
        self.Cancel = QtWidgets.QPushButton(MainScreen)
        self.Cancel.setGeometry(QtCore.QRect(350, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Cancel.setFont(font)
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Dialog"))
        self.label.setText(_translate("MainScreen", "Select an image of a cat or dog"))
        self.Browse.setText(_translate("MainScreen", "Browse"))
        self.Ok.setText(_translate("MainScreen", "OK"))
        self.Cancel.setText(_translate("MainScreen", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QDialog()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
