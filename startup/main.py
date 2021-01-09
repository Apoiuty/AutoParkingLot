#主程序
from PyQt5 import QtCore
from controller.login_controller import LoginController
from PyQt5.QtWidgets import QApplication
import sys

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#保持原始GUI显示
    app = QApplication(sys.argv)
    exit_code = 0
    while True:
        mainwindow = LoginController()#将由控制器创建视图
        exit_code = app.exec_()
        if exit_code == 666:#重新登录码
            continue
        break
    sys.exit(exit_code)

if __name__ == '__main__':
    main()

