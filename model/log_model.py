from db.operation import DatabaseVisitor


class Log_Model():
    """
    日志的控制器，与数据库交互
    """

    def __init__(self):
        self.db = DatabaseVisitor()

    def get_log_data_plate(self, index):
        """
        以车牌信息查询表
        :param index: 车牌信息
        :return:
        """
        index = index.strip()
        sql = "SELECT * FROM SocietyHistory WHERE Scar = '%s'" % (index)
        re = self.db.find_all(sql)
        return re

    def get_log_data_time(self, data):
        """
        以一个时间段查询车辆信息
        :param data: 时间区间,以逗号间隔
        :return:
        """
        data = data.strip()
        if data.startswith('-'):
            data_begin = '2000-00-00 00:00:00'
            data_end = data[0].strip()
        elif data.endswith("-"):
            data_begin = data[0].strip()
            data_end = '2077-06-22 11:11:11'
        elif '-' in data:
            data = data.split('-')
            data_begin = data[0].strip()
            data_end = data[1].strip()
        else:
            print("Inappropriate time intervals.")
        # 查询语句
        sql_begin = "SELECT * FROM SocietyHistory WHERE Sout between '{0}' and '{1}'".format(data_begin, data_end)
        sql_end = "SELECT * FROM SocietyHistory WHERE Sin between '{0}' and '{1}'".format(data_begin, data_end)

        re = self.db.find_all(sql_end)
        re += self.db.find_all(sql_begin)
        re = list(set(re))
        return re
