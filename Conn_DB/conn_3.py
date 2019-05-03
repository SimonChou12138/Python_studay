# encoding=utf-8
# 删除
import MySQLdb
try:
    conn = MySQLdb.connect(host='192.168.1.7', port=3306, db='study', user='root', passwd='123456', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("delete from students where id=2")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print("Exception", e)
