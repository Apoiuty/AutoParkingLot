from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore
from view.login_ui import Ui_login
import sys

class LoginView(QMainWindow,Ui_login):
    def __init__(self):
        super(LoginView, self).__init__()
        self.setupUi(self)

    def get_input_username(self):
        return self.line_input_username.text()

    def get_input_password(self):
        return self.view.line_input_password.text()

    def is_env_home_selected(self):
        return self.view.radiobtn_home.isChecked()

    def is_env_society_selected(self):
        return self.view.radiobtn_society.isChecked()

    def show_input_lack_tips(self):
        self.label_tips.setText('请输入用户名和密码')

    def show_env_tips(self):
        self.label_tips.setText('请选择工作环境')

    def show_login_ok_tips(self):
        self.label_tips.setText("登陆成功")

    def show_input_error_tips(self):
        self.label_tips.setText("用户名或密码错误")

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = LoginView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())