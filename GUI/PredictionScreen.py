# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PredictionScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PredictionWindow(object):
    def setupUi(self, PredictionWindow):
        PredictionWindow.setObjectName("PredictionWindow")
        PredictionWindow.resize(970, 420)
        self.Finish = QtWidgets.QPushButton(PredictionWindow)
        self.Finish.setGeometry(QtCore.QRect(280, 330, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Finish.setFont(font)
        self.Finish.setObjectName("Finish")
        self.label = QtWidgets.QLabel(PredictionWindow)
        self.label.setGeometry(QtCore.QRect(100, 10, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(PredictionWindow)
        QtCore.QMetaObject.connectSlotsByName(PredictionWindow)

    def retranslateUi(self, PredictionWindow):
        _translate = QtCore.QCoreApplication.translate
        PredictionWindow.setWindowTitle(_translate("PredictionWindow", "Dialog"))
        self.Finish.setText(_translate("PredictionWindow", "Finish"))
        self.label.setText(_translate("PredictionWindow", "Your image is a "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PredictionWindow = QtWidgets.QDialog()
    ui = Ui_PredictionWindow()
    ui.setupUi(PredictionWindow)
    PredictionWindow.show()
    sys.exit(app.exec_())
