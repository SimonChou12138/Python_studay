# encoding=utf-8
from conn_封装 import *
from hashlib import *

def login():
    sname = input("请输入用户名:")
    spwd = input("请输入密码:")

    s1 = sha1()
    s1.update(spwd.encode("utf-8"))
    spwdSha1 = s1.hexdigest()

    sql = "select upwd from userInfos where uname='{0}'".format(sname)
    conn = MysqlHelper('192.168.1.7', 3306, 'study', 'root', '123456')
    userinfos = conn.get_one(sql)
    if userinfos == None:
        print("用户名错误")
    elif userinfos[0] == spwdSha1:
        print("登录成功")
    else:
        print("登录失败")

def register():
    sname = input("请输入注册的用户名")
    spwd = input("请输入密码")
    mds = sha1()
    mds.update(spwd.encode("utf-8"))
    spwdsh1 = mds.hexdigest()

    sql = "insert into userInfos(uname, upwd) values('%s','%s')" % (sname, spwdsh1)
    conn = MysqlHelper('192.168.1.7', 3306, 'study', 'root', '123456')
    Infos = conn.insert(sql)
    if Infos == 1:
        print("Success")
        login()
        exit()
    else:
        print("Fail")


if __name__ == '__main__':
    while True:
        choose = int(input("请输入操作数进行操作：1、登录 2、注册"))
        if choose == 1:
            login()
            break
        elif choose == 2:
            register()
        else:
            print("请重新输入")
            continue


