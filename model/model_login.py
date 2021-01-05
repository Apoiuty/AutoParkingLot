from view.ui_login import Ui_login
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import time
from db.operation import DatabaseVisitor

class ModelLogin():
    def __init__(self):
        self.db=DatabaseVisitor()
        self.observer=Ui_login()#订阅的观察者为login的视图


