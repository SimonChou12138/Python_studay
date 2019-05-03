# # 1.以下代码使用递归的方式来生成斐波那契数列：
# def foo(num):
#     if num <= 1:
#         return num
#     else:
#         return foo(num-1)+foo(num-2)
#
# nterms =  int(input("请输入范围"))
# if nterms <= 0:
#     print("请输入整数")
# else:
#     print("斐波那契数列")
#     for i in range(nterms):
#         print(foo(i))
#
# # 2.以下代码演示了Python基本的文件操作，包括 open，read，write：
# while(True):
#     Num = int(input("请输入操作数 1--read 2--write"))
#     if Num == 1:
#         Name = input("请输入文件名字:")
#         with open(Name+".txt", "r") as r:
#             s = r.read()
#             print(s)
#     if Num == 2:
#         Name = input("请输入文件名字:")
#         with open(Name+".txt", "w") as w:
#             w.write("Hello World!")

# 3.Python字符串的判断：
# 测试实例一
print("测试实例一")
str = "WWW.Baidu.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

# 测试实例二
print("测试实例二")
str = "Baidu"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())

# 4.将字符串转换为大写字母，或者将字符串转为小写字母等：
str = "www.Baidu.com"
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())

# 5.以下代码通过导入 calendar 模块来计算每个月的天数：
import calendar
monthRange = calendar.monthcalendar(2019, 5)
monthRange = calendar.monthrange(2019, 3)
print(monthRange)
