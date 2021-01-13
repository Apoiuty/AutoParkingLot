from db.operation import DatabaseVisitor
import sqlite3


def print_result(result):
    for item in result:
        print(item)


# 开发时使用创建
if __name__ == '__main__':
    conn = sqlite3.connect('../Database.db')
    cursor = conn.cursor()
    cursor.close()
    conn.commit()
    conn.close()  #
    dbvisitor = DatabaseVisitor()
    #删除表
    # sql='''DROP TABLE HomeHistory'''
    # dbvisitor.drop_table(sql)

    # 创建小区停车场——历史停车记录表
    # 一个车多次出入，所以主属性是序号自增
    # Hno，记录序号，sql插入时也无需写入Hno属性，他自动递增
    # Hcar车牌号
    # Hflag未完成标志

    # sql = '''CREATE TABLE HomeHistory
    #    (Hno INTEGER PRIMARY KEY,
    #    Hcar VARCHAR(10) ,
    #    Hflag INTEGER,
    #    Hin TIMESTAMP NULL,
    #    Hout TIMESTAMP NULL)'''
    # dbvisitor.create_table(sql)

    # # 创建小区停车-车辆信息表
    # # 以车辆为主属性
    # # Hcarport车位
    # # Howner车主名
    # # Hownerhouse车主住所
    # # Hownerphone车主电话
    # # Hownerkind车主类型：租户或者常住之类的
    # sql = '''CREATE TABLE HomeCar
    #    (Hcar VARCHAR(10) PRIMARY KEY,
    #    Hcarport VARCHAR(10),
    #    Howner VARCHAR(10),
    #    Hownerhouse VARCHAR(25),
    #    Hownerphone VARCHAR(11),
    #    Hownerkind VARCHAR(10))'''
    # dbvisitor.create_table(sql)
    # # 创建社会车场-历史停车记录表
    # #Sno 自动递增主属性，无需sql插入单独写入
    # sql = '''CREATE TABLE SocietyHistory
    #    (Sno INTEGER PRIMARY KEY,
    #    Scar VARCHAR(10)  ,
    #    Sin TIMESTAMP NULL ,
    #    Sout TIMESTAMP NULL ,
    #    Sfee FLOAT,
    #    Srate FLOAT)'''
    # dbvisitor.create_table(sql)
    # # 创建社会车场-当前停车表（待计费，出去计费后，一次停车完成才写入历史停车记录表SocietyHistory)
    # #Sin 自动插入离开时间，无需sql插入单独写入
    # sql = '''CREATE TABLE SocietyCurrent
    #    (Scar VARCHAR(10) PRIMARY KEY ,
    #    Sin TIMESTAMP NOT NULL DEFAULT(datetime('now', 'localtime')),
    #    Srate FLOAT)'''
    # dbvisitor.create_table(sql)
    # # 创建管理员表
    # sql = '''CREATE TABLE User
    #    (Uname VARCHAR(10) PRIMARY KEY ,
    #    Upassword VARCHAR(10),
    #    Urank INT,
    #    Uphone VARCHAR(15))'''
    # dbvisitor.create_table(sql)
    # #插入数据测试
    # sql = '''INSERT INTO User (Uname,Upassword,Urank,Uphone)
    #         VALUES ('worker', 'passwo', 5, '12932277777')'''
    # dbvisitor.update(sql)
    # sql = '''INSERT INTO HomeHistory (Hcar,Hflag,Hin,Hout)
    #             VALUES ('苏Q00012', 1,'2021-01-15 20:56:02', '2021-01-15 22:56:02')'''
    # dbvisitor.update(sql)
    # sql = '''INSERT INTO HomeCar (Hcar,Hcarport,Howner,Hownerhouse,Hownerphone,Hownerkind)
    #                 VALUES ('苏Q00012', 'A08','马某','12-3-501','13963363333','租户')'''
    # dbvisitor.update(sql)
    # sql = '''INSERT INTO SocietyHistory (Scar,Sfee,Sin,Sout,Srate)
    #             VALUES ('苏Q00002', 25,'2021-01-11 20:56:02', '2021-01-12 22:56:02',0.05)'''
    # dbvisitor.update(sql)
    # sql = '''INSERT INTO SocietyCurrent (Scar,Srate)
    #             VALUES ('苏Q00009', 0.05)'''
    # dbvisitor.update(sql)


    # 查看
    sql = "SELECT * FROM User"
    result = dbvisitor.find_all(sql)
    print('User')
    print_result(result)

    sql = "SELECT * FROM HomeHistory"
    result = dbvisitor.find_all(sql)
    print('HomeHistory')
    print_result(result)

    sql = "SELECT * FROM HomeCar"
    result = dbvisitor.find_all(sql)
    print('HomeCar')
    print_result(result)

    sql = "SELECT * FROM SocietyHistory"
    result = dbvisitor.find_all(sql)
    print('SocietyHistory')
    print_result(result)

    sql = "SELECT * FROM SocietyCurrent"
    result = dbvisitor.find_all(sql)
    print('SocietyCurrent')
    print_result(result)
