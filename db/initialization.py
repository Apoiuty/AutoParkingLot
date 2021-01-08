from db.operation import DatabaseVisitor
import sqlite3

def print_result(result):
    for item in result:
        print(item)

#开发时使用创建
if __name__=='__main__':
    conn = sqlite3.connect('../Database.db')
    cursor = conn.cursor()
    cursor.close()
    conn.commit()
    conn.close()#
    dbvisitor=DatabaseVisitor()
    # #创建小区停车场——历史停车表，当前停车表暂不需要
    sql='''CREATE TABLE HomeHistory
       (Hno INTEGER PRIMARY KEY,
       Hcar VARCHAR(10) ,
       Hin TIMESTAMP NOT NULL DEFAULT(datetime('now', 'localtime')) ,
       Hout TIMESTAMP NULL ,
       Howner VARCHAR(10),
       Hplace VARCHAR(10),
       Hownerkind VARCHAR(10))'''
    dbvisitor.create_table(sql)
    # 创建社会车场-历史停车表
    sql='''CREATE TABLE SocietyHistory
       (Sno INTEGER PRIMARY KEY,
       Scar VARCHAR(10)  ,
       Sin TIMESTAMP NOT NULL DEFAULT(datetime('now', 'localtime')) ,
       Sout TIMESTAMP NULL ,
       Sfee FLOAT,
       Srate FLOAT)'''
    dbvisitor.create_table(sql)
    #创建社会车场-当前停车表
    sql='''CREATE TABLE SocietyCurrent
       (Scar VARCHAR(10) PRIMARY KEY ,
       Sin TIMESTAMP NOT NULL DEFAULT(datetime('now', 'localtime')),
       Srate FLOAT)'''
    dbvisitor.create_table(sql)
    #创建管理员表
    sql='''CREATE TABLE User
       (Uname VARCHAR(10) PRIMARY KEY ,
       Upassword VARCHAR(10),
       Urank INT,
       Uphone VARCHAR(15))'''
    dbvisitor.create_table(sql)
    #插入数据测试
    sql='''INSERT INTO User (Uname,Upassword,Urank,Uphone)
            VALUES ('worker01', 'password', 5, '12932277777')'''
    dbvisitor.update(sql)
    sql = '''INSERT INTO HomeHistory (Hcar,Howner,Hout,Hplace)
                VALUES ('苏Q00010', '马某','2021-01-08 20:56:02','A06')'''
    dbvisitor.update(sql)
    sql = '''INSERT INTO SocietyHistory (Scar,Sfee,Sout,Srate)
                VALUES ('苏Q00004', 25, '2021-01-08 22:56:02',0.05)'''
    dbvisitor.update(sql)
    sql = '''INSERT INTO SocietyCurrent (Scar,Srate)
                VALUES ('苏Q00008', 0.05)'''
    dbvisitor.update(sql)
    #查看
    sql="SELECT * FROM User"
    result=dbvisitor.find_all(sql)
    print('User')
    print_result(result)
    sql="SELECT * FROM HomeHistory"
    result=dbvisitor.find_all(sql)
    print('HomeHistory')
    print_result(result)
    sql="SELECT * FROM SocietyHistory"
    result=dbvisitor.find_all(sql)
    print('SocietyHistory')
    print_result(result)
    sql="SELECT * FROM SocietyCurrent"
    result=dbvisitor.find_all(sql)
    print('SocietyCurrent')
    print_result(result)

