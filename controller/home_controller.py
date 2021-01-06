from PyQt5 import QtCore
from view.home_view import HomeView
from model.home_model import HomeModel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class HomeController():
    def __init__(self):
        self.view = HomeView()
        self.model = HomeModel()
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = HomeController()
    sys.exit(app.exec_())
