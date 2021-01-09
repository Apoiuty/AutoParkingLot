from controller.society_controller import SocietyController
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QWidget
from PyQt5 import QtCore,QtGui

class CameraSimulator(QMainWindow):
    def __init__(self,observer):
        self.observer=observer


