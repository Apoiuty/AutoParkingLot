# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(802, 607)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(159, 51, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(575, 51, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_relogin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_relogin.setGeometry(QtCore.QRect(720, 9, 64, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_relogin.setFont(font)
        self.btn_relogin.setObjectName("btn_relogin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(142, 344, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(55, 398, 311, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(54, 452, 311, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(473, 398, 301, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(561, 344, 158, 39))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(472, 452, 301, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(56, 148, 272, 80))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(473, 150, 272, 80))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(157, 99, 102, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_2.setFont(font)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(home)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(home)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(home)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(home)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.action_3.setFont(font)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(home)
        self.action_4.setObjectName("action_4")
        self.action_7 = QtWidgets.QAction(home)
        self.action_7.setObjectName("action_7")
        self.action_9 = QtWidgets.QAction(home)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(home)
        self.action_10.setObjectName("action_10")
        self.action_12 = QtWidgets.QAction(home)
        self.action_12.setVisible(False)
        self.action_12.setObjectName("action_12")
        self.action_6 = QtWidgets.QAction(home)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.action_6.setFont(font)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_12)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_7)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "停车管理系统-小区停车"))
        self.label.setText(_translate("home", "车辆入口"))
        self.label_2.setText(_translate("home", "车辆出口"))
        self.btn_relogin.setText(_translate("home", "重新登录"))
        self.label_3.setText(_translate("home", "入口识别结果"))
        self.label_4.setText(_translate("home", "车牌号码："))
        self.label_5.setText(_translate("home", "车辆信息："))
        self.label_6.setText(_translate("home", "车牌号码："))
        self.label_7.setText(_translate("home", "出口识别结果"))
        self.label_9.setText(_translate("home", "车辆信息："))
        self.menu.setTitle(_translate("home", "管理"))
        self.menu_2.setTitle(_translate("home", "业主"))
        self.menu_3.setTitle(_translate("home", "日志"))
        self.action.setText(_translate("home", "新建管理员"))
        self.action_2.setText(_translate("home", "删除管理员"))
        self.action_3.setText(_translate("home", "添加新信息"))
        self.action_4.setText(_translate("home", "按车辆查询"))
        self.action_7.setText(_translate("home", "按日期查询"))
        self.action_9.setText(_translate("home", "按车主查询"))
        self.action_10.setText(_translate("home", "切换手动模式"))
        self.action_12.setText(_translate("home", "设置"))
        self.action_6.setText(_translate("home", "修改旧信息"))
