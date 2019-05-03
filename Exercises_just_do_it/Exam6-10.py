# 1.以下实例演示了如何生成一个随机数：
import random
print(random.randint(0,10))
# 2.以下实例演示了如何将摄氏温度转华氏温度：
a = float(input("请输入摄氏度"))
b = float(a*1.8+32)
print("华氏温度%0.1f" % b)
# 3.以下实例通过用户输入两个变量，并相互交换：
a = input("请输入x")
b = input("请输入y")
b, a = a, b
print("x:"+a, "y:"+b)
# 4.以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：
a = int(input("请输入一个数字"))
if a > 0:
    print("正数")
elif a < 0:
    print("负数")
else:
    print("零")
# 5.以下实例通过创建自定义函数 is_number() 方法来判断字符串是否为数字：
import unicodedata
def is_number(num):
    try:
        unicodedata.numeric(num)
        return True
    except:
        return False


print(is_number('四'))  # True
print(is_number('©'))  # False
