import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,qApp

from controller.society_controller import SocietyController
from model.home_model import HomeModel
from view.home_view import HomeView
from view.rate_view import rate_view
from controller.add_car_owner_controller import Car_owner_contrl,Car_Owner_Change_Control


class HomeController(SocietyController):
    def __init__(self,current_user):
        self.view = HomeView()
        self.model = HomeModel(self.view)
        self.view.setupUi(self.view)
        self.view.show()  # 控制器创建视图
        self.circumstance = 'home'
        self.current_user = current_user

        #     绑定日志按钮
        self.view.action_4.triggered.connect(lambda: self.Log_menu('plate'))
        self.view.action_7.triggered.connect(lambda: self.Log_menu('time'))
        self.view.action_9.triggered.connect(lambda: self.Log_menu('owner'))
        self.view.action_12.triggered.connect(self.Rate_set)

        # 管理员方法绑定
        self.view.action.triggered.connect(self.add_admin)
        self.view.action_2.triggered.connect(self.delete_admin)
        # 按钮绑定
        self.view.btn_relogin.clicked.connect(self.click_btn_relogin)
        #     添加信息补录菜单
        self.view.action_3.triggered.connect(self.add_owner)
        self.view.action_6.triggered.connect(self.change_owner)


    def add_owner(self):
        """
        信息补录
        :return:
        """
        control = Car_owner_contrl()

    #修改信息
    def change_owner(self):
        control=Car_Owner_Change_Control()

    def click_btn_relogin(self):  # 重新登录点击事件的控制
        re = self.view.ensure_to_quit()
        if re == True:
            self.view.close()
            qApp.exit(666)  # 666是重新登录代码
        else:
            pass

    # def exit(self):
    #     """
    #     退出按钮绑定
    #     :return:
    #     """
    #     sys.exit(self.view)

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
