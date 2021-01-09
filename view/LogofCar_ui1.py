# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogofCar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogByCarName(object):
    def setupUi(self, LogByCarName):
        """
        :param LogByCarName: Qdialog对象
        :return:
        """
        LogByCarName.setObjectName("LogByCarName")
        LogByCarName.resize(852, 1020)
        LogByCarName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        LogByCarName.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label = QtWidgets.QLabel(LogByCarName)
        self.label.setGeometry(QtCore.QRect(300, 40, 341, 41))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(LogByCarName)
        self.widget.setGeometry(QtCore.QRect(92, 93, 628, 851))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CarNameInputPro = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.CarNameInputPro.setFont(font)
        self.CarNameInputPro.setObjectName("CarNameInputPro")
        self.horizontalLayout.addWidget(self.CarNameInputPro)
        self.CarNameInput = QtWidgets.QLineEdit(self.widget)
        self.CarNameInput.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.CarNameInput.setFont(font)
        self.CarNameInput.setText("")
        self.CarNameInput.setObjectName("CarNameInput")
        self.horizontalLayout.addWidget(self.CarNameInput)
        self.CarNameConfirm = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.CarNameConfirm.setFont(font)
        self.CarNameConfirm.setObjectName("CarNameConfirm")
        self.horizontalLayout.addWidget(self.CarNameConfirm)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        # 新建了tabel view窗口
        self.TableOfCarLog = QtWidgets.QTableView(self.widget)
        self.TableOfCarLog.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TableOfCarLog.setObjectName("TableOfCarLog")
        self.verticalLayout.addWidget(self.TableOfCarLog)

        self.retranslateUi(LogByCarName)
        QtCore.QMetaObject.connectSlotsByName(LogByCarName)

    def retranslateUi(self, LogByCarName):
        _translate = QtCore.QCoreApplication.translate
        LogByCarName.setWindowTitle(_translate("LogByCarName", "车辆日志查询"))
        self.label.setText(_translate("LogByCarName",
                                      "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#55aaff;\">车辆进出查询</span></p></body></html>"))
        self.CarNameInputPro.setText(_translate("LogByCarName",
                                                "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">请输入车牌号：</span></p></body></html>"))
        self.CarNameConfirm.setText(_translate("LogByCarName", "查询"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LogByCarName = QtWidgets.QDialog()
    ui = Ui_LogByCarName()
    ui.setupUi(LogByCarName)
    LogByCarName.show()
    sys.exit(app.exec_())
