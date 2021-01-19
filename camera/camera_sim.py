import re
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel

# from controller.home_controller import HomeController
# from controller.society_controller import SocietyController


# 自定义的标签组件，支持拖拽模拟摄像头
class MyQlabel(QLabel):
    signal = pyqtSignal(str)  # 利用信号机制跨组件传递消息

    def __init__(self, _parent=None):
        super().__init__(_parent)
        self.setAcceptDrops(True)  # 控件可以接受其他拖拽过来的内容

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():  # 拖拽过来如果是文本就接受
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        image = e.mimeData().text()
        image = re.sub('^file:///', '', image)
        # print(image)
        if '\n' in image:
            pass
        else:
            self.signal.emit(image)  # 信号发送


# 界面
class Ui_camera(object):
    def setupUi(self, camera):
        camera.setObjectName("camera")
        camera.resize(314, 235)
        self.label_camera_in = MyQlabel(camera)
        self.label_camera_in.setGeometry(QtCore.QRect(58, 25, 240, 70))
        self.label_camera_in.setMouseTracking(True)
        self.label_camera_in.setAcceptDrops(True)
        self.label_camera_in.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_camera_in.setText("")
        self.label_camera_in.setObjectName("label_camera_in")
        self.label = QtWidgets.QLabel(camera)
        self.label.setGeometry(QtCore.QRect(13, 36, 51, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(camera)
        self.label_2.setGeometry(QtCore.QRect(13, 151, 51, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_camera_out = MyQlabel(camera)
        self.label_camera_out.setGeometry(QtCore.QRect(58, 138, 240, 70))
        self.label_camera_out.setMouseTracking(True)
        self.label_camera_out.setAcceptDrops(True)
        self.label_camera_out.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_camera_out.setText("")
        self.label_camera_out.setObjectName("label_camera_out")

        self.retranslateUi(camera)
        QtCore.QMetaObject.connectSlotsByName(camera)

    def retranslateUi(self, camera):
        _translate = QtCore.QCoreApplication.translate
        camera.setWindowTitle(_translate("camera", "摄像头模拟器"))
        self.label.setText(_translate("camera", "进入"))
        self.label_2.setText(_translate("camera", "离开"))


# 是因为模拟摄像头才写的摄像头模拟界面，并不是因为实际如此
class CameraSimulator(QWidget, Ui_camera):
    def __init__(self, observer):
        super().__init__()
        self.observer = observer
        self.setupUi(self)
        self.show()
        self.label_camera_in.signal.connect(self.show_in)  # 截获信号的槽
        self.label_camera_out.signal.connect(self.show_out)

    def show_in(self, path):
        img = QtGui.QPixmap(path).scaled(self.label_camera_in.width(), self.label_camera_in.height())
        self.label_camera_in.setPixmap(img)
        self.notify_observer_in_msg(path)  # 通知观察者有变

    def show_out(self, path):
        img = QtGui.QPixmap(path).scaled(self.label_camera_out.width(), self.label_camera_out.height())
        self.label_camera_out.setPixmap(img)
        self.notify_observer_out_msg(path)  # 通知观察者有变

    def notify_observer_in_msg(self, path):
        self.observer.identify_in_car(path)

    def notify_observer_out_msg(self, path):
        self.observer.identify_out_car(path)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    #window = CameraSimulator(SocietyController())
    #window.show()  # 显示窗口
    sys.exit(app.exec_())
