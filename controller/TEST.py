from db.operation import DatabaseVisitor

# ndbvisitor = DatabaseVisitor()
# #sql = "SELECT * FROM User "
# sql="SELECT Upassword FROM User WHERE Uname = 'worker01'"
# db_password = ndbvisitor.find_one(sql)
# print(db_password)
# from PyQt5.QtWidgets import QMainWindow
#
# class Ui_login(QMainWindow):

from PyQt5 import QtCore
from view.login_view import LoginView
from model.login_model import LoginModel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
from db.operation import DatabaseVisitor


class ControllerLogin():
    def __init__(self, model):
        self.view = LoginView()
        self.model = model  # LoginModel()这里model作为参数传入
        self.view.setupUi(self.view)
        self.view.btn_login.clicked.connect(lambda: self.click_btn_login())
        self.view.show()  # 控制器创建视图

    # 登录动作
    def click_btn_login(self):
        # 获取login_view信息
        input_username = self.view.line_input_username.text()
        input_password = self.view.line_input_password.text()
        env_society = self.view.radiobtn_society.isChecked()
        env_home = self.view.radiobtn_home.isChecked()
        # 向模型发出控制信号
        self.model.try_to_login(input_username, input_password, env_society, env_home)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    model=LoginModel()
    mainwindow = ControllerLogin(model)
    sys.exit(app.exec_())
