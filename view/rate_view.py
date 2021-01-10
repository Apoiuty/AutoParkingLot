import configparser

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QSlider

from view.pure_ui.rate_ui import Ui_Rate


class rate_view(QDialog, Ui_Rate):
    """
    设置费率
    """

    def __init__(self, mode):
        """
        费率设置
        :param mode: 小区还是社会
        """
        QDialog.__init__(self)
        self.setupUi(self)
        #         设置调整范围，最大为10，最小为0，每格0.5
        self.RateSlider.setMaximum(20)
        self.RateSlider.setMinimum(0)
        self.RateSlider.setTickInterval(1)
        self.RateSlider.setTickPosition(QSlider.TicksAbove)
        self.DoubleSpin.setRange(0, 10)
        self.DoubleSpin.setSingleStep(0.5)

        # 读取数据文件
        self.mode = mode
        self.config = configparser.ConfigParser()
        # 写成相对路径
        self.config.read('../config.ini', encoding='utf-8')
        init_value = self.config.getfloat('sys', mode)
        self.RateSlider.setValue(int(init_value * 2))
        self.DoubleSpin.setValue(init_value)

        #         绑定方法
        self.RateSlider.valueChanged.connect(self.changeSpinBox)
        self.DoubleSpin.valueChanged.connect(self.changeSlider)

        self.pushButton.clicked.connect(self.setRate)

        self.exec_()

    def changeSpinBox(self):
        """
        更改显示框的值
        :return:
        """
        self.DoubleSpin.valueChanged.disconnect(self.changeSlider)
        self.DoubleSpin.setValue(float(self.RateSlider.value()) / 2.0)
        self.DoubleSpin.valueChanged.connect(self.changeSlider)

    def changeSlider(self):
        """
        更改滑动条的值
        :return:
        """
        self.RateSlider.valueChanged.disconnect(self.changeSpinBox)
        self.RateSlider.setValue(int((self.DoubleSpin.value()) * 2))
        self.RateSlider.valueChanged.connect(self.changeSpinBox)

    def setRate(self):
        """
        设置费率
        :return:
        """
        value = self.DoubleSpin.value()
        self.config.set('sys', self.mode, str(value))
        self.config.write(open('../config.ini', 'w'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = rate_view('home_society')
    ui.show()
    sys.exit(app.exec_())
