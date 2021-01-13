import sqlite3


# 数据库访问类
class DatabaseVisitor():
    def __init__(self, db='../Database.db'):
        self._conn = None
        self._cursor = None
        self._db = db

    # 连接数据库
    def connect(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()

    # 关闭游标和连接
    def close(self):
        self._cursor.close()
        self._conn.close()

    # 创建表
    def create_table(self, sql):
        self.connect()
        try:
            self._cursor.execute(sql)  # 游标执行
            self._conn.commit()  # 执行完提交
            print("create table ok")
            return True
        except:
            print("create table error")
            return False
        finally:
            self.close()

    # 删除表
    def drop_table(self, sql):
        self.connect()
        try:
            self._cursor.execute(sql)
            self._conn.commit()
            return True
        except:
            print('drop_table error')
            return False
        finally:
            self.close()

    # 查询所有符合条件数据，返回一个列表
    def find_all(self, sql):
        self.connect()
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
            return result
        except:
            print('find_all error')
            return []
        finally:
            self.close()

    # 只查询一个
    def find_one(self, sql):
        self.connect()
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchone()
            return result
        except:
            print('find_one error')
            return False
        finally:
            self.close()

    # 增删改
    def update(self, sql):
        self.connect()
        try:
            self._cursor.execute(sql)
            self._conn.commit()
            return True
        except:
            print('update error')
            return False
        finally:
            self.close()
