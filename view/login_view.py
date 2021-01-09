from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore
from view.pure_ui.login_ui import Ui_login
import sys

class LoginView(QMainWindow,Ui_login):
    def __init__(self):
        super(LoginView, self).__init__()
        self.setupUi(self)

    def get_input_username(self):
        re=self.line_input_username.text()
        return re

    def get_input_password(self):
        re=self.line_input_password.text()
        return re

    def is_env_home_selected(self):
        re=self.radiobtn_home.isChecked()
        return re

    def is_env_society_selected(self):
        re=self.radiobtn_society.isChecked()
        return re

    def show_input_lack_tips(self):
        self.label_tips.setText('请输入用户名和密码')

    def show_env_tips(self):
        self.label_tips.setText('请选择工作环境')

    def show_login_ok_tips(self):
        self.label_tips.setText("登陆成功")

    def show_input_error_tips(self):
        self.label_tips.setText("用户名或密码错误")

    def show_input_so_long_tips(self):
        self.label_tips.setText("用户名和密码过长")

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = LoginView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())