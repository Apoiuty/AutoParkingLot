from PyQt5 import QtCore
from view.society_view import SocietyView
from model.society_model import SocietyModel
from PyQt5.QtWidgets import QApplication, qApp
import sys


class SocietyController():
    def __init__(self):
        self.view = SocietyView()
        self.model = SocietyModel()
        self.view.setupUi(self.view)
        self.view.btn_relogin.clicked.connect(lambda: self.click_btn_relogin())
        self.view.show()  # 控制器创建视图
        self.new_view = None
        self.rate = 0.05

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


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = SocietyController()
    sys.exit(app.exec_())
