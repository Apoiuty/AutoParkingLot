# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'society_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_society(object):
    def setupUi(self, society):
        society.setObjectName("society")
        society.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(society.sizePolicy().hasHeightForWidth())
        society.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(society)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(153, 52, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(568, 52, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_relogin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_relogin.setGeometry(QtCore.QRect(697, 9, 87, 26))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.btn_relogin.setFont(font)
        self.btn_relogin.setObjectName("btn_relogin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(139, 268, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(51, 322, 341, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(51, 376, 361, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(469, 322, 301, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(558, 268, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(469, 376, 311, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(469, 424, 311, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_in_car = QtWidgets.QLabel(self.centralwidget)
        self.label_in_car.setGeometry(QtCore.QRect(140, 320, 281, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_in_car.setFont(font)
        self.label_in_car.setText("")
        self.label_in_car.setObjectName("label_in_car")
        self.label_in_time = QtWidgets.QLabel(self.centralwidget)
        self.label_in_time.setGeometry(QtCore.QRect(140, 380, 261, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_in_time.setFont(font)
        self.label_in_time.setText("")
        self.label_in_time.setObjectName("label_in_time")
        self.label_out_car = QtWidgets.QLabel(self.centralwidget)
        self.label_out_car.setGeometry(QtCore.QRect(560, 320, 221, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_out_car.setFont(font)
        self.label_out_car.setText("")
        self.label_out_car.setObjectName("label_out_car")
        self.label_fee = QtWidgets.QLabel(self.centralwidget)
        self.label_fee.setGeometry(QtCore.QRect(560, 420, 231, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_fee.setFont(font)
        self.label_fee.setText("")
        self.label_fee.setObjectName("label_fee")
        self.label_out_time = QtWidgets.QLabel(self.centralwidget)
        self.label_out_time.setGeometry(QtCore.QRect(560, 370, 221, 38))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_out_time.setFont(font)
        self.label_out_time.setText("")
        self.label_out_time.setObjectName("label_out_time")
        self.label_in_img = QtWidgets.QLabel(self.centralwidget)
        self.label_in_img.setGeometry(QtCore.QRect(55, 139, 272, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_in_img.setFont(font)
        self.label_in_img.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_in_img.setText("")
        self.label_in_img.setObjectName("label_in_img")
        self.label_out_img = QtWidgets.QLabel(self.centralwidget)
        self.label_out_img.setGeometry(QtCore.QRect(470, 139, 272, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_out_img.setFont(font)
        self.label_out_img.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_out_img.setText("")
        self.label_out_img.setObjectName("label_out_img")
        self.line_handmode_car_in = QtWidgets.QLineEdit(self.centralwidget)
        self.line_handmode_car_in.setGeometry(QtCore.QRect(72, 153, 153, 36))
        self.line_handmode_car_in.setObjectName("line_handmode_car_in")
        self.line_handmode_car_out = QtWidgets.QLineEdit(self.centralwidget)
        self.line_handmode_car_out.setGeometry(QtCore.QRect(487, 153, 153, 36))
        self.line_handmode_car_out.setObjectName("line_handmode_car_out")
        self.btn_handmode_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_handmode_in.setGeometry(QtCore.QRect(240, 153, 71, 35))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.btn_handmode_in.setFont(font)
        self.btn_handmode_in.setObjectName("btn_handmode_in")
        self.btn_handmdoe_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_handmdoe_out.setGeometry(QtCore.QRect(655, 153, 71, 35))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.btn_handmdoe_out.setFont(font)
        self.btn_handmdoe_out.setObjectName("btn_handmdoe_out")
        self.label_in_car.raise_()
        self.label_in_time.raise_()
        self.label_out_car.raise_()
        self.label_out_time.raise_()
        self.label_fee.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btn_relogin.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_in_img.raise_()
        self.label_out_img.raise_()
        self.line_handmode_car_in.raise_()
        self.line_handmode_car_out.raise_()
        self.btn_handmode_in.raise_()
        self.btn_handmdoe_out.raise_()
        society.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(society)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(169, 99, 147, 132))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_2.setFont(font)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_4.setFont(font)
        self.menu_4.setObjectName("menu_4")
        society.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(society)
        self.statusbar.setObjectName("statusbar")
        society.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(society)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(society)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(society)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.action_3.setFont(font)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(society)
        self.action_4.setObjectName("action_4")
        self.action_7 = QtWidgets.QAction(society)
        self.action_7.setObjectName("action_7")
        self.action_9 = QtWidgets.QAction(society)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(society)
        self.action_10.setObjectName("action_10")
        self.action_12 = QtWidgets.QAction(society)
        self.action_12.setObjectName("action_12")
        self.action_5 = QtWidgets.QAction(society)
        self.action_5.setObjectName("action_5")
        self.action_8 = QtWidgets.QAction(society)
        self.action_8.setObjectName("action_8")
        self.action_hand_mode = QtWidgets.QAction(society)
        self.action_hand_mode.setObjectName("action_hand_mode")
        self.action_auto_mode = QtWidgets.QAction(society)
        self.action_auto_mode.setObjectName("action_auto_mode")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu_3.addAction(self.action_4)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_7)
        self.menu_3.addSeparator()
        self.menu_2.addAction(self.action_5)
        self.menu_2.addSeparator()
        self.menu_4.addAction(self.action_hand_mode)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_auto_mode)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(society)
        QtCore.QMetaObject.connectSlotsByName(society)

    def retranslateUi(self, society):
        _translate = QtCore.QCoreApplication.translate
        society.setWindowTitle(_translate("society", "停车管理系统-社会停车模式"))
        self.label.setText(_translate("society", "车辆入口"))
        self.label_2.setText(_translate("society", "车辆出口"))
        self.btn_relogin.setText(_translate("society", "重新登录"))
        self.label_3.setText(_translate("society", "入口识别结果"))
        self.label_4.setText(_translate("society", "车牌号码："))
        self.label_5.setText(_translate("society", "进入时间："))
        self.label_6.setText(_translate("society", "车牌号码："))
        self.label_7.setText(_translate("society", "出口识别结果"))
        self.label_9.setText(_translate("society", "离开时间："))
        self.label_10.setText(_translate("society", "应收费用："))
        self.btn_handmode_in.setText(_translate("society", "输入车牌"))
        self.btn_handmdoe_out.setText(_translate("society", "输入车牌"))
        self.menu.setTitle(_translate("society", "管理"))
        self.menu_3.setTitle(_translate("society", "日志"))
        self.menu_2.setTitle(_translate("society", "费用"))
        self.menu_4.setTitle(_translate("society", "模式"))
        self.action.setText(_translate("society", "新建管理员"))
        self.action_2.setText(_translate("society", "删除管理员"))
        self.action_3.setText(_translate("society", "信息补录"))
        self.action_4.setText(_translate("society", "按车辆查询"))
        self.action_7.setText(_translate("society", "按日期查询"))
        self.action_9.setText(_translate("society", "按车主查询"))
        self.action_10.setText(_translate("society", "切换手动模式"))
        self.action_12.setText(_translate("society", "设置"))
        self.action_5.setText(_translate("society", "费率设置"))
        self.action_8.setText(_translate("society", "收费统计"))
        self.action_hand_mode.setText(_translate("society", "切换到手动模式"))
        self.action_auto_mode.setText(_translate("society", "切换到自动模式"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    society = QtWidgets.QMainWindow()
    ui = Ui_society()
    ui.setupUi(society)
    society.show()
    sys.exit(app.exec_())
