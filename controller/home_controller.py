import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from controller.Car_log_controller import LogController
from model.home_model import HomeModel
from view.home_view import HomeView
from view.rate_view import rate_view


class HomeController():
    def __init__(self):
        self.view = HomeView()
        self.model = HomeModel()
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图
        self.circumstance = 'home'

        #     绑定日志按钮
        self.view.action_4.triggered.connect(lambda: self.Log_menu('plate'))
        self.view.action_7.triggered.connect(lambda: self.Log_menu('time'))
        self.view.action_9.triggered.connect(lambda: self.Log_menu('owner'))
        self.view.action_12.triggered.connect(self.Rate_set)

    def Log_menu(self, mode):
        """
        日志菜单功能实现
        :param mode:
        :return:
        """
        log_dialog = LogController(self.circumstance, mode)

    def Rate_set(self):
        """
        设置费率文件
        :return:
        """
        rate_set = rate_view('home_rate')


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = HomeController()
    sys.exit(app.exec_())
