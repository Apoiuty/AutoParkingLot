# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_owner_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Car_owner(object):
    def setupUi(self, Car_owner):
        Car_owner.setObjectName("Car_owner")
        Car_owner.resize(479, 350)
        self.gridLayout = QtWidgets.QGridLayout(Car_owner)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Car_owner)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(7)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_plate = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_plate.setFont(font)
        self.label_plate.setObjectName("label_plate")
        self.horizontalLayout_6.addWidget(self.label_plate)
        self.lineEdit_type_2 = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_type_2.setFont(font)
        self.lineEdit_type_2.setObjectName("lineEdit_type_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_type_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_pos = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_pos.setFont(font)
        self.label_pos.setObjectName("label_pos")
        self.horizontalLayout_2.addWidget(self.label_pos)
        self.lineEdit_pos = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_pos.setFont(font)
        self.lineEdit_pos.setObjectName("lineEdit_pos")
        self.horizontalLayout_2.addWidget(self.lineEdit_pos)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_home = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_home.setFont(font)
        self.label_home.setObjectName("label_home")
        self.horizontalLayout_3.addWidget(self.label_home)
        self.lineEdit_home = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_home.setFont(font)
        self.lineEdit_home.setObjectName("lineEdit_home")
        self.horizontalLayout_3.addWidget(self.lineEdit_home)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_phone = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.horizontalLayout_4.addWidget(self.label_phone)
        self.lineEdit_phone = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.horizontalLayout_4.addWidget(self.lineEdit_phone)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_type = QtWidgets.QLabel(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout_5.addWidget(self.label_type)
        self.lineEdit_type = QtWidgets.QLineEdit(Car_owner)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_type.setFont(font)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.horizontalLayout_5.addWidget(self.lineEdit_type)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Car_owner)
        QtCore.QMetaObject.connectSlotsByName(Car_owner)

    def retranslateUi(self, Car_owner):
        _translate = QtCore.QCoreApplication.translate
        Car_owner.setWindowTitle(_translate("Car_owner", "添加新信息"))
        self.pushButton.setText(_translate("Car_owner", "确定"))
        self.label_name.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">车主姓名：</span></p></body></html>"))
        self.label_plate.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">车牌号码：</span></p></body></html>"))
        self.label_pos.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">对应车位：</span></p></body></html>"))
        self.label_home.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">车主住所：</span></p></body></html>"))
        self.label_phone.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">车主电话：</span></p></body></html>"))
        self.label_type.setText(_translate("Car_owner", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">车主类型：</span></p></body></html>"))
