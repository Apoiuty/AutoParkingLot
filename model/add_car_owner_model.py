from db.operation import DatabaseVisitor


class Carowner_model():

    def __init__(self, observer):
        self.db = DatabaseVisitor()
        self.observer = observer

    def check_carplate(self, carplate):  # 检查传入车牌合法性
        PLATE_CHARS_PROVINCE = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑",
                                "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤",
                                "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁",
                                "新", "警", "军", "甲", "W"]
        # 这些是合法的字符
        PLATE_CHARS_LETTER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
                              "J",
                              "K", "L", "M", "N", "P",
                              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        # 首先检查长度
        if len(carplate) != 7:
            return False
        # #检查车牌首字符,考虑到特种车辆（虽然可能不会停进来）,放到后面一并检查
        # if carplate[0] not in PLATE_CHARS_PROVINCE :
        #     return False
        # 检查车牌字符是否在合法字符集中
        for i in range(0, 7):
            if carplate[i] not in PLATE_CHARS_LETTER and carplate[i] not in PLATE_CHARS_PROVINCE:
                return False
        return True

    def check_empty(self,info):#输入完整判断
        #print(info)
        for i in range(6):
            if info[i]=='':
                return False
        return True

    def write_car_owner(self, items):
        """
        写入数据库中新增车主的信息
        :param items: 车主信息元组
        :return:
        """
        re1 = self.check_empty(items) #检查输入完整
        re2=self.check_carplate(items[1])#检查车牌号码
        if re1==False:
            self.observer.show_msg('请您输入完整信息')
        elif re2==False:
            self.observer.show_msg('请您确保正确输入车牌字符')
        else:#通过适当检查才写入
            sql = "insert into HomeCar (Hcar,Hcarport,Howner,\
            Hownerhouse,Hownerphone,Hownerkind) values " \
                  "('{1}','{2}','{0}','{3}','{4}','{5}')".format(*items)
            re=self.db.update(sql)#尝试写入
            #写入反馈
            if re==True:
                self.observer.show_msg('添加新信息成功')
            else:
                self.observer.show_msg('添加新信息失败，请检查输入或者信息已经存在，可以修改旧信息')

    def change_car_info(self,items):
        re1 = self.check_empty(items) #检查输入完整
        re2=self.check_carplate(items[1])#检查车牌号码
        if re1==False:
            self.observer.show_msg('请您输入完整信息')
        elif re2==False:
            self.observer.show_msg('请您确保正确输入车牌字符')
        else:#通过适当检查才写入
            sql="select Howner from HomeCar where Hcar='{1}'".format(*items)
            result=self.db.find_one(sql)
            print(result)
            if result==None or result==False:
                self.observer.show_msg('无此车辆对应信息，您可以考虑使用添加新信息功能')
            else:
                sql = "update HomeCar set Hcar='{1}',Hcarport='{2}',Howner='{0}',Hownerhouse='{3}',Hownerphone='{4}',Hownerkind='{5}' where Hcar='{1}'"\
                       .format(*items)
                re=self.db.update(sql)#尝试写入
                #写入反馈
                if re==True:
                    self.observer.show_msg('修改旧信息成功')
                else:
                    self.observer.show_msg('修改旧信息失败，请检查输入或该信息不存在，请选择添加')

