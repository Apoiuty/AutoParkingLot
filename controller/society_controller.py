from PyQt5 import QtCore

from controller.Car_log_controller import LogController
from view.society_view import SocietyView
from model.society_model import SocietyModel
from PyQt5.QtWidgets import QApplication, qApp
import sys
from view.rate_view import rate_view


class SocietyController():
    def __init__(self):
        self.view = SocietyView()
        self.model = SocietyModel()
        self.view.setupUi(self.view)
        self.view.btn_relogin.clicked.connect(lambda: self.click_btn_relogin())
        self.view.show()  # 控制器创建视图
        self.new_view = None
        self.rate = 0.05

        # 菜单方法绑定
        self.view.action_4.triggered.connect(lambda: self.Log_menu('plate'))
        self.view.action_7.triggered.connect(lambda: self.Log_menu('time'))
        self.view.action_9.triggered.connect(lambda: self.Log_menu('owner'))
        self.view.action_5.triggered.connect(self.Rate_set)

    def click_btn_relogin(self):  # 重新登录
        re = self.view.ensure_to_quit()
        if re == True:
            self.view.close()
            qApp.exit(666)  # 666是重新登录代码
        else:
            pass

    def identify_in_car(self, img):
        result = self.model.identify_result(img)
        self.view.show_in_car(result)  # 改变视图显示
        self.view.show_in_time()
        self.view.show_in_img(img)

    def identify_out_car(self, img):
        result = self.model.identify_result(img)
        self.view.show_out_car(result)  # 改变视图显示
        self.view.show_out_time()
        self.view.show_out_img(img)

    def Rate_set(self):
        """
        设置费率文件
        :return:
        """
        rate_set = rate_view('society_rate')

    def Log_menu(self, mode):
        """
        日志菜单功能实现
        :param mode:
        :return:
        """
        log_dialog = LogController(mode)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = SocietyController()
    sys.exit(app.exec_())
