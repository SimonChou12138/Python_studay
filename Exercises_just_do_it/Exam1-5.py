import math
import cmath
# 1.输出"Hello World!"
print("Hello World")
# 2.以下实例为通过用户输入两个数字，并计算两个数字之和：
a = int(input("输入一个数字:"))
b = int(input("输入一个数字:"))
c = a + b
print(c)
# 3.平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
# 以下实例为通过用户输入一个数字，并计算这个数字的平方根：
a = float(input("请输入一个数字"))
b = math.sqrt(a)
print(b)
# 4.以下实例为通过用户输入数字，并计算二次方程：
a = float(input("请输入一个数字"))
b = float(input("请输入一个数字"))
b = float(input("请输入一个数字"))
d = (b**2)-(4*a*c)
e = (-b+cmath.sqrt(d))/(2*a)
f = (-b-cmath.sqrt(d))/(2*a)

print(e)
print(f)
# 5.以下实例为通过用户输入三角形三边长度，并计算三角形的面积：
# a = float(input("请输入底边长度"))
# b = float(input("请输入一个高度"))
# s = (a*b)*0.5
# print(s)
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)


