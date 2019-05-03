# 1.通过导入 datetime 模块来获取昨天的日期：
import datetime
def yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

print(yesterday())
# 2.list的常用操作

# 2.1 list的定义
li = ["a", "b", "c"]
print(li)
# 2.2 list的负数索引
print(li[-1])
print(li[-2])
# 2.3 list 增加元素
print(li.append("d"))
# 2.4 list 搜索
print(li.index("a"))
# 2.5 list 删除元素
print(li.remove("a"))
# 2.6 list 运算符
temp = ["e"]
print(li+temp)
# 2.7 使用join链接list成为字符串
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print([";".join(["%s=%s" % (k, v) for k, v in params.items()])])
# 2.8 list 分割字符串
str = "123;456;789"
print(str.split(';'))
print(",".join([k for k in str.split(";")]))
# 2.9 list 的映射解析
li = [1, 4, 6, 8]
print([i**2 for i in li])
# 2.10 dictionary 中的解析
li = {1, 4, 6, 8}
print([i+2 for i in li])
# 2.11 list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([k for k in li if len(k) > 1])
