# # 1.整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
# num = 1
# for i in range(1, 4):
#     num *= i
# print(num)
# # 2.九九乘法表
# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print("{0} * {1} = {2}".format(i, j, i*j), end="")
# # 3.斐波那契数列
# a = 0
# b = 1
# Max = int(input("请输入一个数"))
# for i in range(1, Max+1):
#     print(a)
#     b, a = a+b, b
# 4.如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
for i in range(1, 1000):
    Len = len(str(i))
    if Len == 1 and i == i ** Len:
        print(i)
    elif Len == 2 and i == i % 10 ** Len + i / 10 ** Len:
        print(i)
    elif Len == 3 and i == i % 100 / 10 ** Len + i % 10 ** Len + i / 100 ** Len:
        print(i)
# for num in range(1, 1000):
#     sum = 0
#     n = len(str(num))
#
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** n
#         temp //= 10
#
#     if num == sum:
#         print(num)
# 5.实现十进制转二进制、八进制、十六进制：
a = 10
a2 = bin(a)
a8 = oct(a)
a16 = hex(a)
print("{0}二进制 {1}八进制 {2}十六进制".format(a2, a8, a16))