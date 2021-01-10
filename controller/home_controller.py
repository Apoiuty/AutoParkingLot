from PyQt5 import QtCore
from view.home_view import HomeView
from model.home_model import HomeModel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from controller.add_admin_controller import AddAdminController
from controller.delete_admin_controller import DeleteAdminController

class HomeController():
    def __init__(self):
        self.view = HomeView()
        self.model = HomeModel()
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图
        self.view.action.triggered.connect(self.add_admin)
        self.view.action_2.triggered.connect(self.delete_admin)

    def add_admin(self):
        am = AddAdminController()
    def delete_admin(self):
        dm = DeleteAdminController()
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = HomeController()
    sys.exit(app.exec_())
