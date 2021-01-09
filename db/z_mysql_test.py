import pymysql


class DatabaseVisitor:  # 数据库访问类
    def __init__(self, host, user, password, database, charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.cursor = None
        self.db_conn = None

    # 建立连接，返回游标
    def connect(self):
        self.db_conn = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                       database=self.database, charset=self.charset)
        self.cursor = self.db_conn.cursor()
        print('connected')

    # 关闭游标和连接
    def close(self):
        self.cursor.close()
        self.db_conn.close()

    # 查找操作
    def find(self, sql):
        self.connect()
        try:
            cnt = self.cursor.execute(sql)  # 通过游标执行sql语句，返回记录数
            result = self.cursor.fetchall()
            print('find success')
            return result
        except:
            print('find error')
        finally:
            self.close()

    # 更新：增删改
    def update(self, sql):
        self.connect()
        try:
            cnt = self.cursor.execute(sql)
            self.database.commit()
            print('update success')
            return cnt
        except:
            print('update error')
            self.database.rollback()  # 更新失败数据回滚
        finally:
            self.close()


if __name__ == '__main__':
    db_visitor = DatabaseVisitor(host='localhost', user='root',
                                 password='cs2022', database='parking_db', charset='utf8mb4')
    sql = "SELECT * FROM user"
    re = db_visitor.find(sql)
    print(re)
