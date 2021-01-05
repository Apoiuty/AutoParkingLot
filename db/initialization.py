from db.operation import DatabaseVisitor
import sqlite3
#开发时使用创建
if __name__=='__main__':

    conn = sqlite3.connect('../Database.db')
    cursor = conn.cursor()
    cursor.close()
    conn.commit()
    conn.close()#
    dbvisitor=DatabaseVisitor()
    sql='''CREATE TABLE House
       (Hcar VARCHAR(10) PRIMARY KEY ,
       Howner VARCHAR(10), 
       Hplace VARCHAR(10), 
       Hownerkind VARCHAR(10))'''
    dbvisitor.create_table(sql)
    sql='''CREATE TABLE Social
       (Scar VARCHAR(10) PRIMARY KEY ,
       Sin DATETIME, 
       Sout DATETIME, 
       Sfee FLOAT,
       Srate FLOAT)'''
    dbvisitor.create_table(sql)
    sql='''CREATE TABLE User
       (Uname VARCHAR(10) PRIMARY KEY ,
       Upassword VARCHAR(10), 
       Urank INT, 
       Uphone VARCHAR(15))'''
    dbvisitor.create_table(sql)
    sql='''INSERT INTO User (Uname,Upassword,Urank,Uphone)
            VALUES ('worker01', 'password', 5, '12932277777')'''
    dbvisitor.update(sql)
    sql="SELECT * FROM User"
    result=dbvisitor.find_all(sql)
    print(result)