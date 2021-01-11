from db.operation import DatabaseVisitor
from cnn.identifier import identify_car_plate
class SocietyModel():
    def __init__(self,observer):
        self.db=DatabaseVisitor()
        self.observer=observer

    def identify_result(self,path,flag):
        result=identify_car_plate(path)
        self.notify_observer_result_condition(result,flag)#通知视图观察者识别状态改变

    def notify_observer_result_condition(self,result_msg,flag):
        if flag==0:#车辆进入识别
            self.observer.show_in_car(result_msg)
            self.observer.show_in_time()
        else:
            self.observer.show_out_car(result_msg)
            self.observer.show_out_time()

    #下面是数据库相关操作






