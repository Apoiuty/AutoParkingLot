import sqlite3

from db.operation import DatabaseVisitor

class DeleteAdminModel():
    def __init__(self):
        self.db=DatabaseVisitor()
        self.observer=[]

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
    def try_to_select(self,uname):

        dbvisitor = DatabaseVisitor()
        sql = "select * from  User where Uname = \"%s\""%(uname)
        re = dbvisitor.update(sql)
        print(re)
        if not re:
            return False
        else:
            return True