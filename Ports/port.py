"""
定义了主程序中需要调用的函数接口
"""


# 算法实现
def LPR(license):
    """
    输入车牌图像（图像文件）,返回车牌信息
    :param license: *.jpg(png)
    :return: 车牌字符串
    """
    pass


# GUI实现
def GUI_init():
    """
    GUI界面初始化
    :return: none
    """
    pass


def show_position():
    """
    显示可用的位置
    :return:
    """


# 数据库
def W_database(license, time):
    """
    入库时将车辆信息写入数据库，time为开始停车时间（具体实现参考time模块）
    :param license: 车牌字符
    :param time: 开始停车时间
    :return: bool 是否操作成功
    """
    pass


def Register(license):
    """
    对于初次驶入的车辆进行注册
    :param license: 车牌字符串
    :return: bool 是否操作成功
    """
    pass


def R_database(license):
    """
    从数据库中读取车辆信息
    :param license: 车牌字符串
    :return: 表示车辆信息的列表，返回的信息包括车辆的各种信息\\TODO
    """
    pass


def D_database(license):
    """
    出库时删除车辆的停车信息
    :param license:车牌信息
    :return: none
    """
    pass


def black_list(license):
    """
    将车辆写入黑名单
    :param license: 车牌信息
    :return: none
    """


def Get_time(time):
    """
    从数据库中读取某一时间入库的车辆信息
    :param time: 时间
    :return: 列表
    """
    pass


# 日志系统
def Write_log(log):
    """
    将log写入日志，log可以是字符对象或是其他对象（可在实现时决定）
    :param log: 日志对象
    :return: bool
    """


def Read_log(time):
    """
    读取某一个时间的日志
    :param time: 时间
    :return: 日志
    """
    pass


# 服务端
def login():
    """
    实现管理员的登录
    :return: none
    """
    pass


def payment(license):
    """
    对车辆进行计费
    :param license: 车牌信息
    :return: none
    """
    pass
