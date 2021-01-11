from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QHeaderView, QMessageBox

from view.pure_ui.LogofCar_ui import Ui_LogByCarName
from view.pure_ui.LogoofCar_time import Ui_LogByTime


class carnameLog(QDialog, Ui_LogByCarName):
    """
    日志查询类
    """

    def __init__(self):
        """
        窗体初始化
        :param dialog: 对话框
        """
        QDialog.__init__(self)
        self.setupUi(self)
        # 设置未查找到提示框
        self.message = QMessageBox()

    def set_tabel(self, items, circu):
        """
        设置table view的显示查询信息
        :param circu:
        :param items:查询到的列表
        :return:
        """
        if not items:
            self.message.warning(self, "提示", "未找到日志记录", QMessageBox.Yes)
            return

        items = [i[1:-1] for i in items]
        row = len(items)
        col = len(items[0])

        model = QStandardItemModel(row, col)

        table_head = ['车牌', '进入时间', '离去时间', '收费']
        model.setHorizontalHeaderLabels(table_head)

        for i in range(row):
            for j in range(col):
                item = QStandardItem(str(items[i][j]))
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                model.setItem(i, j, item)

        self.TableOfCarLog.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TableOfCarLog.setModel(model)


class carTimeLog(Ui_LogByTime, carnameLog):
    """
    通过时间来查询车辆日志
    """

    def getDateTime(self):
        return self.dateTime_begin.dateTime().toString(
            "yyyy-MM-dd hh:mm:ss") + ',' + self.dataTime_end.dateTime().toString(
            "yyyy-MM-dd hh:mm:ss")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = carTimeLog()
    ui.show()
    sys.exit(app.exec_())
