# encoding=utf-8
import MySQLdb


class MysqlHelper():
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        self.conn = MySQLdb.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print("Exception", e)
        return result

    def get_all(self, sql):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print("Exception", e)
        return list

    def insert(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print("Exception", e)
        return count