# encoding=utf-8
# 增加
import MySQLdb
try:
    conn = MySQLdb.connect(host='192.168.1.7', port=3306, db='study', user='root', passwd='123456', charset='utf8')
    # 用于数据库的读取
    cs1 = conn.cursor()
    # 执行数据库代码并返回响应行数
    count = cs1.execute("insert into students(sname) values('张良')")
    print(count)
    # 提交代码
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print("Exception", e)

