import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont

ui_path = os.path.join(os.path.dirname(__file__), "Animal Classifier.ui")
desktop_path = os.path.expanduser("~/Desktop")

class MainScreen(QDialog):

    def __init__(self):
        super().__init__()
        loadUi(ui_path, self)

        self.Browse.clicked.connect(self.browsefiles)

        self.show()
    
    def browsefiles(self):

        filter_type = "Images (*.png *.xpm *.jpg *.jfif)"

        filename = QFileDialog.getOpenFileName(self, "File Explorer", desktop_path, filter=filter_type)
        file_path = filename[0]
        self.Filepath.setText(file_path)

        return file_path
            

app = QApplication([])
main_screen = MainScreen()

app.exec_()

#FINISHED: BROWSING THROUGH FILES

#TO DO: ADD PREDICTION WINDOW BASED ON IMAGE
#       ADD PICTURE OF IMAGE INTO WINDOW