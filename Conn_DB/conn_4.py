# encoding=utf-8
# 语句参数化
import MySQLdb
try:
    conn = MySQLdb.connect(host='192.168.1.7', port=3306, db='study', user='root', passwd='123456', charset='utf8')
    cur = conn.cursor()
    sname = input("请输入你要增加的学生名字：")
    count = cur.execute("insert into students(sname) values('%s')" % (sname))
    print(count)

    # stable = input("请输入你要查询的表名")
    # cur.execute("select * from %s" % (stable))
    # result = cur.fetchall()# 多行查询
    # result = cur.fetchone()# 单行查询
    # print(result)

    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(e)