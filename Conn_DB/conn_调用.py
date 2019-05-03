# encoding=utf-8
from conn_封装 import *
sname = input("请输入添加的学生姓名")
sql = "insert into students(sname) values('{0}')".format(sname)

conn = MysqlHelper('192.168.1.7', 3306, 'study', 'root', '123456')
count = conn.insert(sql)
if count == 1:
    print("success")
else:
    print("fail")

# 查询全部
# sql = 'select sname from students order by id desc'
# helper = MysqlHelper('192.168.1.7', 3306, 'study', 'root', '123456')
# all = helper.get_all(sql)
# print(all)
