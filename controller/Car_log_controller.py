import sys

from PyQt5 import QtCore, QtWidgets

from model.log_model import Log_Model
from view.LogofCar_view import carnameLog, carTimeLog


class LogController():
    """
    日志控制器
    """

    def __init__(self, circumstance, mode):
        """
         控制器初始化
        :param circumstance:
        :param mode: 是车牌查询还是日期查询
        """
        mode_index = {'plate': '请输入车牌号', 'time': '请输入停车时间', 'owner': '请输入车主姓名'}
        self.mode = mode
        self.circumstance = circumstance
        if self.mode != 'time':
            self.view = carnameLog()
        else:
            self.view = carTimeLog()
        self.model = Log_Model(self.view)

        # 修改标签提示内容
        self.view.CarNameConfirm.clicked.connect(self.get_log_data)
        _translate = QtCore.QCoreApplication.translate
        if self.mode != 'time':
            self.view.CarNameInputPro.setText(_translate("carnameLog",
                                                         "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">" +
                                                         mode_index[mode] + "：</span></p></body></html>"))

        if self.mode == 'owner':
            self.view.label.setText(_translate("LogByCarName", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55aaff;\">请输入车主信息</span></p></body></html>"))

        self.view.exec_()

    def get_log_data(self):
        """
        获取输入的信息并查询记录
        :return:
        """
        if self.mode != 'time':
            query_item = self.view.CarNameInput.text()
        else:
            query_item = self.view.getDateTime()

        # 获取输入信息并查询项目
        if self.mode == 'plate':
            self.model.get_log_data_plate(query_item, self.circumstance)
        elif self.mode == 'time':
            self.model.get_log_data_time(query_item, self.circumstance)
        else:
            self.model.get_log_data_owner(query_item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = LogController('home', 'time')
    sys.exit(app.exec_())
