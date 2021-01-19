from PyQt5 import QtCore
from view.add_admin_view import AddAdminView
from model.add_admin_model import AddAdminModel
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
import sys


class AddAdminController():
    def __init__(self,current_user):
        self.view = AddAdminView()
        self.model = AddAdminModel()
        self.view.setupUi(self.view)
        # 绑定函数
        self.view.add.clicked.connect(lambda: self.click_add())
        self.view.show()  # 控制器创建视图
        self.new_view = None
        self.current_user = current_user
        # print("add")
        # print(self.current_user)

    # 登录控制
    def click_add(self):
        input_username = self.view.get_input_username()  # 获取视图login_view信息
        input_password = self.view.get_input_password()
        double_password = self.view.get_input_doublepassword()
        input_userrank = self.view.get_input_urank()  # 获取视图login_view信息
        input_userphone = self.view.get_input_uphone()

        if (input_username == ""):
            self.view.mes(message="未输入用户名", mode="information")
        elif (input_password == ""):
            self.view.mes(message="未输入密码", mode="information")
        elif (input_password != double_password):
            self.view.mes(message="两次密码不一致", mode="critical")
        elif len(input_username) > 25 or len(input_password) > 25:
            self.view.mes(message="密码长度太长", mode="critical")
        elif (input_userrank == ""):
            self.view.mes(message="未输入等级", mode="information")
        elif(self.view.get_input_urank() <= str(self.model.search_rank(self.current_user))):
            self.view.mes(message="等级权限不够,无法创建等级高的管理员", mode="information")
        elif (input_userphone == ""):
            self.view.mes(message="未输入电话", mode="information")
        elif(self.model.is_existed(input_username)):
            self.view.mes(message="用户已存在", mode="information")
        else:
            flag = self.model.try_to_add(input_username, input_password, input_userrank, input_userphone)
            if flag:
                self.view.mes(message="创建管理员成功!", mode="information")
                self.view.clear_input()
            else:
                self.view.mes(message="创建管理员失败!", mode="information")


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = AddAdminController()
    sys.exit(app.exec_())
    # exit_code=app.exec_()
    # sys.exit(exit_code)
