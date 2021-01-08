from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QWidget
from PyQt5 import QtCore,QtGui
from view.society_ui import Ui_society
import sys
from PIL import Image

class SocietyView(QMainWindow,Ui_society):
    def __init__(self):
        super(SocietyView, self).__init__()
        self.setupUi(self)

    def ensure_to_quit(self):
        reply=QMessageBox.question(self,'Message','确定要退出重新登录吗?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            return True
        else:
            return False

    def show_in_car(self,result):
        self.label_in_car.setText(result)

    def show_out_car(self,result):
        self.label_out_car.setText(result)

    def show_in_time(self):
        time = QtCore.QDateTime.currentDateTime()
        time = time.toString("yyyy-MM-dd hh:mm:ss")
        self.label_in_time.setText(time)

    def show_out_time(self):
        time = QtCore.QDateTime.currentDateTime()
        time = time.toString("yyyy-MM-dd hh:mm:ss")
        self.label_out_time.setText(time)

    def show_in_img(self,path):
        jpg = QtGui.QPixmap(path).scaled(self.label_in_img.width(), self.label_in_img.height())
        self.label_in_img.setPixmap(jpg)

    def show_out_img(self,path):
        jpg = QtGui.QPixmap(path).scaled(self.label_out_img.width(), self.label_out_img.height())
        self.label_out_img.setPixmap(jpg)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = SocietyView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())