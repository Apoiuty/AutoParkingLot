from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore
from view.login_ui import Ui_login
import sys

class LoginView(QMainWindow,Ui_login):
    def __init__(self):
        super(LoginView, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 如果是启动文件，则创建 Application 实例 app
    window = LoginView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())