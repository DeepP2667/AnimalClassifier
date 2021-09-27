import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PredictionWindow(object):
    def setupUi(self, PredictionWindow):
        PredictionWindow.setObjectName("PredictionWindow")
        PredictionWindow.resize(1026, 541)
        self.Finish = QtWidgets.QPushButton(PredictionWindow, clicked=lambda: sys.exit())
        self.Finish.setGeometry(QtCore.QRect(190, 370, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Finish.setFont(font)
        self.Finish.setObjectName("Finish")
        self.Prediction = QtWidgets.QLabel(PredictionWindow)
        self.Prediction.setGeometry(QtCore.QRect(100, 70, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Prediction.setFont(font)
        self.Prediction.setObjectName("Prediction")
        self.Image = QtWidgets.QLabel(PredictionWindow)
        self.Image.setGeometry(QtCore.QRect(600, 80, 581, 391))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Image.setFont(font)
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("../../../../../../Cat.jpg"))
        self.Image.setObjectName("Image")

        self.retranslateUi(PredictionWindow)
        QtCore.QMetaObject.connectSlotsByName(PredictionWindow)

    def retranslateUi(self, PredictionWindow):
        _translate = QtCore.QCoreApplication.translate
        PredictionWindow.setWindowTitle(_translate("PredictionWindow", "Dialog"))
        self.Finish.setText(_translate("PredictionWindow", "Finish"))
        self.Prediction.setText(_translate("PredictionWindow", "Your image is a "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PredictionWindow = QtWidgets.QDialog()
    ui = Ui_PredictionWindow()
    ui.setupUi(PredictionWindow)
    PredictionWindow.show()
    sys.exit(app.exec_())
