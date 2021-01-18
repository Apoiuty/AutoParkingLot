# 主程序
from PyQt5 import QtCore
from controller.login_controller import LoginController
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
import sys

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    exit_code = 0
    while True:
        mainwindow = LoginController()
        exit_code = app.exec_()
        if exit_code == 666:
            continue
        break
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
