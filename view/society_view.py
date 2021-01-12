from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt5 import QtCore,QtGui
from view.pure_ui.society_ui import Ui_society
import sys


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

    def msgbox_to_check_handmode_input(self):
        reply = QMessageBox.question(self, 'Message', '请输入正确车牌号格式',QMessageBox.Yes , QMessageBox.Yes)

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

    def open_hand_mode(self):#切换手动模式
        self.clear_view()
        self.label_in_img.setVisible(False)
        self.label_out_img.setVisible(False)
        self.line_handmode_car_in.setVisible(True)#模式切换时让手动模式组件可见
        self.line_handmode_car_out.setVisible(True)
        self.btn_handmdoe_out.setVisible(True)
        self.btn_handmode_in.setVisible(True)
        self.action_hand_mode.setEnabled(False)#菜单栏显示改变
        self.action_auto_mode.setEnabled(True)


    def open_auto_mode(self):#切换自动模式
        self.clear_view()
        self.line_handmode_car_in.setVisible(False)#模式切换时让自动模式组件可见
        self.line_handmode_car_out.setVisible(False)
        self.btn_handmdoe_out.setVisible(False)
        self.btn_handmode_in.setVisible(False)
        self.label_in_img.setVisible(True)
        self.label_out_img.setVisible(True)
        self.action_auto_mode.setEnabled(False)#菜单栏显示改变
        self.action_hand_mode.setEnabled(True)

    def get_handmode_car_in(self):#手动模式下提供用户输入的接口，屏蔽视图实现细节，被控制器调用
        car=self.line_handmode_car_in.text()
        return car

    def get_handmode_car_out(self):
        car = self.line_handmode_car_out.text()
        return car

    def clear_input_handmode_car_in(self):#输入后清除输入框，视图自身不调用，被控制器调用
        self.line_handmode_car_in.setText('')

    def clear_input_handmode_car_out(self):
        self.line_handmode_car_out.setText('')

    def clear_view(self):#清空视图输入显示
        self.label_in_img.clear()
        self.label_out_img.clear()
        self.label_in_car.clear()
        self.label_out_car.clear()
        self.label_in_time.clear()
        self.label_out_time.clear()
        self.label_fee.clear()




if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 创建 Application 实例 app
    window = SocietyView()
    window.show()                 # 显示窗口
    sys.exit(app.exec_())