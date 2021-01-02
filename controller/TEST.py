from db.operation import DatabaseVisitor

ndbvisitor = DatabaseVisitor()
#sql = "SELECT * FROM User "
sql="SELECT Upassword FROM User WHERE Uname = 'worker01'"
db_password = ndbvisitor.find_one(sql)
print(db_password)