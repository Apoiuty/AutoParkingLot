import sqlite3

from db.operation import DatabaseVisitor

class AddAdminModel():
    def __init__(self):
        self.db=DatabaseVisitor()
        self.observer=[]

    def try_to_add(self,uname,upassword,urank,uphone):

        dbvisitor = DatabaseVisitor()
        sql = "insert into User(Uname,Upassword,Urank,Uphone) values(\"%s\",\"%s\",\"%s\",\"%s\")"%(uname,upassword,urank,uphone)
        re = dbvisitor.update(sql)
        if not re:
            return False
        else:
            return True
        # conn = sqlite3.connect('Database.db')
        # conn.execute(sql)
        # conn.commit()
        # conn.close()