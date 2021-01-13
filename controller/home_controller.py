import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from controller.society_controller import SocietyController
from model.home_model import HomeModel
from view.home_view import HomeView
from view.rate_view import rate_view


class HomeController(SocietyController):
    def __init__(self):
        self.view = HomeView()
        self.model = HomeModel(self.view)
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图
        self.circumstance = 'home'

        #     绑定日志按钮
        self.view.action_4.triggered.connect(lambda: self.Log_menu('plate'))
        self.view.action_7.triggered.connect(lambda: self.Log_menu('time'))
        self.view.action_9.triggered.connect(lambda: self.Log_menu('owner'))
        self.view.action_12.triggered.connect(self.Rate_set)

        # 管理员方法绑定
        self.view.action.triggered.connect(self.add_admin)
        self.view.action_2.triggered.connect(self.delete_admin)
        # 退出按钮绑定
        self.view.pushButton.clicked.connect(self.exit)

    def exit(self):
        """
        退出按钮绑定
        :return:
        """
        sys.exit(self.view)

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
