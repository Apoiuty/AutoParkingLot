from PyQt5 import QtCore
from view.society_view import SocietyView
from model.society_model import SocietyModel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class SocietyController():
    def __init__(self):
        self.view = SocietyView()
        self.model = SocietyModel()
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = SocietyController()
    sys.exit(app.exec_())
