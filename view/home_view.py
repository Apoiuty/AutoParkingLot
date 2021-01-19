import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox

from view.pure_ui.home_ui import Ui_home


class HomeView(QMainWindow, Ui_home):
    def __init__(self):
        super(HomeView, self).__init__()
        self.setFixedSize(802,607)
        self.setupUi(self)

    def exit(self):
        """
        退出按钮绑定
        :return:
        """
        self.exit()

    def show_in_car(self, result):
        self.label_4.setText("车牌号码: " + result)
        self.label_5.setText("车辆信息：" + str(datetime.now())[:-7])

    def show_out_car(self, result):
        self.label_6.setText("车牌号码: " + result)
        self.label_9.setText("车辆信息：" + str(datetime.now())[:-7])

    def show_in_img(self, path):
        jpg = QtGui.QPixmap(path).scaled(self.label_8.width(), self.label_8.height())
        self.label_8.setPixmap(jpg)

    def show_out_img(self, path):
        jpg = QtGui.QPixmap(path).scaled(self.label_10.width(), self.label_10.height())
        self.label_10.setPixmap(jpg)

    def ensure_to_quit(self):
        reply = QMessageBox.question(self, 'Message', '确定要退出重新登录吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = HomeView()
    window.show()  # 显示窗口
    sys.exit(app.exec_())
