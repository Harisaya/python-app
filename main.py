from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("home.ui", self)

        self.image1 = self.findChild(QLabel, "image1")
        self.image1.mousePressEvent = self.go_to_dish_ui

    def go_to_dish_ui(self, event):
        self.dish_window = QMainWindow()
        uic.loadUi("dish.ui", self.dish_window)
        self.dish_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())