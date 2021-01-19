import sqlite3

from db.operation import DatabaseVisitor
from view.delete_admin_view import DeleteAdminView
class DeleteAdminModel():
    def __init__(self):
        self.db=DatabaseVisitor()
        self.observer=[]

    def is_existed(self,uname):
        dbvisitor = DatabaseVisitor()
        select_sql="select * from User where Uname= \"%s\""%(uname)
        if not dbvisitor.find_all(select_sql):
            return False
        return True

    def try_to_delete(self,uname):
        dbvisitor = DatabaseVisitor()
        sql = "delete from  User where Uname = \"%s\""%(uname)
        re = dbvisitor.update(sql)
        if not re:
            return False
        else:
            return True
        # conn = sqlite3.connect('Database.db')
        # conn.execute(sql)
        # conn.commit()
        # conn.close()
    def search_rank(self,uname):
        dbvisitor = DatabaseVisitor()
        sql = "select * from  User where Uname = \"%s\"" % (uname)
        re = dbvisitor.find_one(sql)

        return re[2]
