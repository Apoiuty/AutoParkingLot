import unittest
from model.login_model import LoginModel
from model.delete_admin_model import DeleteAdminModel
from model.add_admin_model import AddAdminModel
from model.log_model import Log_Model
from model.home_model import HomeModel
from model.add_car_owner_model import Carowner_model
from model.society_model import SocietyModel

class MyTestCase(unittest.TestCase):
    def test_login(self):
        res  = LoginModel.try_to_login(self,input_username="worker",input_password="passwo")
        self.assertEqual(True, res)

    def test_add_admin(self):
        res= AddAdminModel.try_to_add(self,uname="worker03",upassword="1",urank="6",uphone="12345678956")
        self.assertEqual(True,res)
    # 与原有代码有冲突，测试成功需要屏蔽observer的代码
    # def test_log(self):
    #     res = Log_Model.get_log_data_owner(self,"马测试")
    #     self.assertEqual([('湘A11111', 'A99', '马测试', '1-2-601', '18972275678', '租户')],res)

    # def test_home(self):
    #     res = HomeModel.identify_result()
    #     self.assertEqual(True,)

    # def test_carowner_home(self):
    #     res = Carowner_model.write_car_owner(self,)
    #     self.assertEqual(True,res)
    def test_society(self):
        res = SocietyModel.get_rate(self)
        self.assertEqual(str(1.5),res)
    def test_delete_admin(self):
        res = DeleteAdminModel.try_to_delete(self, uname="1")
        self.assertEqual(True, res)
if __name__ == '__main__':
    unittest.main()
