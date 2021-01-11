import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, qApp

from controller.Car_log_controller import LogController
from model.society_model import SocietyModel
from view.rate_view import rate_view
from view.society_view import SocietyView

class SocietyController():
    def __init__(self):
        self.view = SocietyView()
        self.model = SocietyModel(self.view)
        self.view.setupUi(self.view)
        self.view.btn_relogin.clicked.connect(lambda: self.click_btn_relogin())
        self.view.show()  # 控制器创建视图
        self.new_view = None
        self.rate = 0.05
        self.circumstance = 'society'

        # 菜单方法绑定
        self.view.action_4.triggered.connect(lambda: self.Log_menu('plate'))
        self.view.action_7.triggered.connect(lambda: self.Log_menu('time'))
        self.view.action_9.triggered.connect(lambda: self.Log_menu('owner'))
        self.view.action_5.triggered.connect(self.Rate_set)
        # 菜单方法-模式切换绑定

    def click_btn_relogin(self):  # 重新登录
        re = self.view.ensure_to_quit()
        if re == True:
            self.view.close()
            qApp.exit(666)  # 666是重新登录代码
        else:
            pass

    def identify_in_car(self, img):
        self.view.show_in_img(img)
        self.model.identify_result(img, 0)  # 0是进入标志

    def identify_out_car(self, img):
        self.view.show_out_img(img)
        self.model.identify_result(img, 1)  # 1是出标志


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
        log_dialog = LogController(self.circumstance, mode)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = SocietyController()
    sys.exit(app.exec_())
