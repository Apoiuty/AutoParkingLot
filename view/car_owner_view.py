from view.pure_ui.car_owner_ui import Ui_Car_owner

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QHeaderView, QMessageBox


class Car_Owner(QDialog, Ui_Car_owner):
    """
    新建物主信息类
    """

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(479,350)
        self.message = QMessageBox()

    def get_name(self):
        """
        获取业主名字
        :return:
        """
        return self.lineEdit_name.text()

    def get_pos(self):
        return self.lineEdit_pos.text()

    def get_phone(self):
        return self.lineEdit_phone.text()

    def get_type(self):
        return self.lineEdit_type.text()

    def get_home(self):
        return self.lineEdit_home.text()

    def get_input(self):
        """
        返回输入的车辆信息元组
        :return:
        """
        return self.get_name(), self.get_plate(), self.get_pos(), self.get_home(), \
               self.get_phone(), self.get_type()

    def get_plate(self):
        return self.lineEdit_type_2.text()

    def clear_input(self):
        self.lineEdit_pos.clear()
        self.lineEdit_home.clear()
        self.lineEdit_name.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_type.clear()
        self.lineEdit_type_2.clear()

    #信息展示
    def show_msg(self,msg):
        reply = QMessageBox.question(self, 'Message', msg, QMessageBox.Yes, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False
