# 1.以下实例用于判断一个数字是否为奇数或偶数：
num = int(input("请输入一个数字"))
if num % 2 == 0:
    print("偶数")
elif num % 2 != 0:
    print("奇数")
# 2.以下实例用于判断用户输入的年份是否为闰年：
year = int(input("请输入年份"))
if year % 4 == 0 & year % 100 == 0:
    if year % 400 == 0:
        print("{0}世纪闰年".format(year))
    else:
        print("{0}普通闰年".format(year))
else:
    print("{0}不是闰年".format(year))
# 3.以下实例中我们使用max()方法求最大值：
arr = [1, 2, 3, 4, 7]
print(max(arr))
# 4.一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等
# 换句话说就是该数除了1和它本身以外不再有其他的因数。
num = int(input("请输入一个数字"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("{0}不是质数".format(num))
            break
    else:
        print("{0}是质数".format(num))
# 5.素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
Max = int(input("请输入一个数字"))
for num in range(1, Max+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
