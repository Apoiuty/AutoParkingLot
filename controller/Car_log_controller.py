from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from view.LogofCar_view import carnameLog
from model.log_model import Log_Model
import sys


class LogController():
    """
    日志控制器
    """

    def __init__(self, mode):
        """
         控制器初始化
        :param mode: 是车牌查询还是日期查询
        """
        mode_index = {'plate': '请输入车牌号', 'time': '请输入停车时间', 'owner': '请输入车主姓名'}
        self.mode = mode
        self.view = carnameLog()
        self.model = Log_Model()
        # 设置未查找到提示框
        self.message = QMessageBox()
        # 修改标签提示内容
        self.view.CarNameConfirm.clicked.connect(self.get_log_data)
        _translate = QtCore.QCoreApplication.translate
        self.view.CarNameInputPro.setText(_translate("carnameLog",
                                                     "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">" +
                                                     mode_index[mode] + "：</span></p></body></html>"))
        self.view.exec_()

    def get_log_data(self):
        """
        获取输入的信息并查询记录
        :return:
        """
        Query_item = self.view.CarNameInput.text()
        # 获取输入信息并查询项目
        if self.mode == 'plate':
            re = self.model.get_log_data_plate(Query_item)
        else:
            re = self.model.get_log_data_time(Query_item)

        if re:
            # 输出查询到的车辆信息
            self.view.set_tabel(re)
        else:
            # todo:没有查询到弹出无记录
            self.message.warning(self.view, "提示", "未找到日志记录", QMessageBox.Yes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = LogController('time')
    sys.exit(app.exec_())
