from view.login_view import LoginView
from db.operation import DatabaseVisitor


class LoginModel():
    def __init__(self):
        self.db = DatabaseVisitor()
        self.observer = []

    def try_to_login(self, input_username, input_password):
        dbvisitor = DatabaseVisitor()
        sql = "SELECT Upassword FROM User WHERE Uname = '%s'" % (input_username)
        re = dbvisitor.find_one(sql)
        if re == None or re == False:
            return False
        db_password = re[0]
        if input_password == db_password:
            return True
        else:
            return False
