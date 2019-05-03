# 1.实现ASCII码与字符相互转换：
C = input("请输入一个字符")
A = int(input("请输入一个ASCII"))
print(ord(C))
print(chr(A))
# 2.实现最大公约数算法：
def MaxNum(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y
    for i in range(1,smaller+1):
        if x % i == 0 and y % i == 0:
            Max = i
    return Max


x = int(input("请输入一个整数"))
y = int(input("请输入一个整数"))
print(MaxNum(x, y))
# 3.实现最小公倍数算法：
def MinNum(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if greater % x == 0 and greater % y == 0:
            Min = greater
            break
        greater+=1
    return Min


x = int(input("请输入一个整数"))
y = int(input("请输入一个整数"))
print(MinNum(x, y))
# 4.简单计算器实现
def add(x, y):
    add = x + y
    return add

def subtraction(x, y):
    sub = x - y
    return sub

def multiplication(x, y):
    multip = x * y
    return multip

def division(x, y):
    div = x // y
    return div
while(True):
    Num = int(input("请输入一个操作数 1--加法 2--减法 3--乘法 4--除法"))
    if Num == 1:
        x = int(input("请输入一个整数"))
        y = int(input("请输入一个整数"))
        print(add(x, y))
    elif Num == 2:
        x = int(input("请输入一个整数"))
        y = int(input("请输入一个整数"))
        print(subtraction(x, y))
    elif Num == 3:
        x = int(input("请输入一个整数"))
        y = int(input("请输入一个整数"))
        print(multiplication(x, y))
    elif Num == 4:
        x = int(input("请输入一个整数"))
        y = int(input("请输入一个整数"))
        print(division(x, y))
    elif Num == 0:
        break
# 5.用于生成指定日期的日历：
import calendar
year = int(input("请输入年份"))
Mon = int(input("请输入月份"))
print(calendar.month(year, Mon))
