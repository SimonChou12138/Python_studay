# 1、执行Python脚本的两种方式
# python3 hello.py
# cat hello.py |python

# 2、简述位、字节的关系
# 位：计算机的计算单位，代表0或者1  字节：一字节相当于8位

# 3、简述ascii、unicode、utf-8、gbk的关系

# 4、请写出"李杰"分别用utf-8和gbk编码所占的位数
print(len(bytes("周民帅", encoding="utf-8")))
print(len(bytes("周民帅", encoding="gbk")))

# 5、Python单行注释和多行注释分别用什么？
# 单行注释： # 被注释内容
''' 多行注释 被注释内容 '''

# 6、声明变量注意事项有哪些？
'''
1）由字母、数字和下划线构成，不能以数字开头，不能任意特殊字符
2）变量定义规范，使用驼峰式或者下划线式格式
3）变量定义尽量简明，易懂，方便使用者应用
'''

# 7、利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码
import random
temp = ''
for i in range(4):
    n = random.randrange(0, 2)
    if n == 0:
        # 英文
        num = random.randrange(65, 91)
        temp += chr(num)
    elif n == 1:
        # 数字
        k = random.randrange(0, 10)
        temp += str(k)
print(temp)

# 8、如何查看变量在内存中的地址？
name = "Simon"
print(id(name))

# 9、执行Python程序时，自动生成的.pyc文件的作用是什么？
# python执行前生成的编译字节码文件

# 10、a.实现用户输入用户名和密码，当用户名为 Simon且密码为123时，显示登陆成功，否则登陆失败！(可以失败三次 && 名字可以是chou)
# chance = 3
# while True:
#     userName = input("请输入用户名")
#     passWord = input("请输入密码")
#     if userName == "Simon" or userName == "Chou" and passWord == "123":
#         print("登录成功")
#     else:
#         if chance == 0:
#             break
#         print("登录失败")
#         chance -= 1

# 11、使用while循环实现输出2-3+4-5+6.....+100的和
i = 2
count = 0
while i <= 100:
    if i % 2 == 0:
        count += i
    else:
        count -= i
    i += 1
print("Sum：{0}".format(count))

# 12、求1-2+3-4+5 ... 99的所有数的和
count = 0
for i in range(1, 99+1):
    if i % 2 != 0:
        count += i
    else:
        count -= i
print("Sum:{0}".format(count))

# 13、使用while循环输入 1 2 3 4 5 6     8 9 10
for i in range(1, 10+1):
    if i == 7:
        continue
    else:
        print(i)

# 14、输出1-100内的所有奇数
for i in range(1, 100+1):
    if i % 2 != 0:
        print("{0},".format(i), end="")

# 15、分别书写数字5, 10, 32, 7的二进制表示
a = [5, 10, 32, 7]
for i in a:
    print(i, ":", bin(i))

# 16、现有如下两个变量，请简述n1和n2是什么关系？
# 两个变量引用同一个内存地址
n1 = 123
n2 = 123
print(id(n1), id(n2))
# 1582456464 1582456464

# 两个变量引用同一个内存地址
n1 = 123456
n2 = n1
print(id(n1), id(n2))
# 1990112 1990112

# 17、如有一个变量n1 = 5，请使用int的提供的方法，得出该变量至少可以用多少个二进制位表示？
temp = 6
print(len(bytes(temp)))

# 18、布尔值分别有什么？
# 真 假
# True False
# 0 1

# 19、阅读代码，请写出执行结果
a = "alex"
b = a.capitalize()
print(a)
print(b)

'''
20、写代码，有如下变量，请按照要求实现每个功能
a.移除name变量对应的值两边的空格，并输入移除有的内容
b.判断name变量对应的值是否以 "al"开头，并输出结果
c.判断name变量对应的值是否以 "X"结尾，并输出结果
d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
e.将name变量对应的值根据 " l" 分割，并输出结果。
f.请问，上一题 e分割之后得到值是什么类型？
g.将name变量对应的值变大写，并输出结果
h.将name变量对应的值变小写，并输出结果
i.请输出name变量对应的值的第2个字符？
j.请输出name变量对应的值的前3个字符？
k.请输出name变量对应的值的后2个字符？
l.请输出name变量对应的值中 "e" 所在索引位置？
'''
name = " aleX "
print(name.strip())
print(name.startswith("al"))
print(name.endswith("X"))
print(name.replace("l", "p"))
print(name.split('l'))
print(type(name.split('l')))
print(name.upper())
print(name.lower())
print(name[2])
print(name[:3])
print(name[-2:])
print(name.index("e"))

# 21、字符串是否可迭代？如可以请使用for循环每一个元素？
name = "Simon"
for i in name:
    print(i)

# 22、请代码实现：利用下划线将列表的每一个元素拼接成字符串
li = ['alex', 'eric', 'rain']
print("_".join([i for i in li]))

'''
23、写代码，有如下列表，按照要求实现每一个功能（所有练习题同样适用于元组）

li = ['Simon','eric','rain']    
a.计算列表长度并输出
b.列表中追加元素"seven"，并输出添加后的列表
c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
e.请删除列表中的元素"eric"，并输出修改后的列表
f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
g.请删除列表中的第3个元素，并输出删除元素后的列表
h.请删除列表中的第2至4个元素，并输出删除元素后的列表
i.请将列表所有的元素反转，并输出反转后的列表
j.请使用for、len、range 输出列表的索引
k.请使用enumrate输出列表元素和序号（序号从 100 开始）
l.请使用for循环输出列表的所有元素
'''
li = ['Simon', 'eric', 'rain']
print(len(li))
li.append("seven")
print(li)
li.insert(0, "Tony")
print(li)
li[1] = "Kelly"
print(li)
li.remove("eric")
print(li)
del(li[1])
print(li)
del(li[2])
print(li)
del(li[1:3])
print(li)
li = ['Simon', 'eric', 'rain']
li.reverse()
print(li)
for i in range(len(li)):
    print(i)
for K, V in enumerate(li, 1):
    print("K：{0}，V：{1}".format(K, V))
for i in li:
    print("{0},".format(i), end="")

# 24、写代码，有如下列表，请按照功能要求实现每一个功能
# a.请输出"Kelly"
# b.请使用索引找到 'all'元素并将其修改为"ALL"
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][1][1])
index = li[2].index("all")
li[2][index] = "ALL"
print(li)

# 25、有如下变量，请实现要求的功能
'''
a. 讲述元祖的特性  元组具有列表的全部特性，不同的是，元组的元素不能修改
b. 请问 tu 变量中的第一个元素 "alex" 是否可被修改？  不能因为是元组里的元素
c. 请问 tu 变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven" 可以,列表
d. 请问 tu 变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"  元组，不可以修改
'''
tu = ("alex", [11, 22, {"k1" : 'v1', "k2": ["age", "name"], "k3":(11, 22, 33)}, 44])
tu[1][2]["k2"].append("cc")
print(tu)

# 26、字典
'''
a. 请循环输出所有的 key
b. 请循环输出所有的 value
c. 请循环输出所有的 key 和 value
d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
for k in dic.keys():
    print(k)
for v in dic.values():
    print(v)
for k, v in dic.items():
    print(k, ",", v)
dic["k4"] = "v4"
print(dic)
dic["k1"] = "alex"
print(dic)
dic["k3"].append(44)
print(dic)
dic["k3"].insert(1, 18)
print(dic)

# 27、转换
# a. 将字符串 s="alex" 转换成列表
# b. 将字符串 s="alex" 转换成元祖
# b. 将列表 li=["alex","seven"] 转换成元组
# c. 将元祖 tu=('Alex',"seven") 转换成列表
# d. 将列表 li=["alex","seven"] 转换成字典且字典的 key 按照 10 开始向后递增
s = "Simon"
li = []
for i in s:
    li.append(i)
print(li)
s = "Simon"
print(tuple(s))
li = ["alex", "seven"]
print(tuple(li))
tu = ('Alex', "seven")
li = []
for i in tu:
    li.append(i)
print(li)
tu = ('Alex', "seven")
li_dic = {}
for k, v in enumerate(li, 10):
    li_dic[k] = v
print(li_dic)
# 27、转码
# n="老男孩"
# a. 将字符串转换成 utf-8 编码的字节，并输出，然后将该字节再转换成 utf-8 编码字符串，再输出
# a. 将字符串转换成 gbk 编码的字节，并输出，然后将该字节再转换成 gbk 编码字符串，再输出
n = "老男孩"
print(n.encode("utf-8"))
print(n.encode("utf-8").decode("utf-8"))
print(n.encode("gbk"))
print(n.encode("gbk").decode("gbk"))

# 28、求 1-100 内的所有数的和
sum = 0
for i in range(1, 100+1):
    sum+=i
print(sum)

# 29、元素分类
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
# 即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}
li_dic = {}
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
li1 = []
li2 = []
for i in li:
    if i > 66:
        li1.append(i)
    else:
        li2.append(i)
li_dic['k1'] = li1
li_dic['k2'] = li2
print(li_dic)

# 30、购物车
# 功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods=[
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
money = float(input("请输入总资产"))
print("商品如下")
for k, v in enumerate(goods, 1):
    print(k, ",", v)
num = int(input("请输入商品编号"))
if num == 1:
    for i in goods[0].values():
        try:
            if float(i) <= money:
                print("success")
            else:
                print("None")
        except:
            continue


# 31、查找元素，移除空格，并查找以 a或A开头 并且以 c 结尾的所有元素
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
# for i in li:
#     if i.strip().capitalize().startswith("a", "A") and i.strip().endswith("c"):
#         print(i)
# for i in tu:
#     if i.strip().capitalize().startswith("a", "A") and i.strip().endswith("c"):
#         print(i)
# for i in dic:
#     if i.strip().capitalize().startswith("a", "A") and i.strip().endswith("c"):
#         print(i)
for i in li:
    if i.strip().capitalize().startswith('A') and i.strip().endswith('c'):
        print(i.strip())
for i in tu:
    if i.strip().capitalize().startswith('A') and i.strip().endswith('c'):
        print(i.strip())
for i in dic.values():
    if i.strip().capitalize().startswith('A') and i.strip().endswith('c'):
        print(i.strip())
#32、用户交互，显示省市县三级联动的选择
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "湖南": {
        "长沙": ['a', 'b', 'c'],
        "株洲": ['d', 'e', 'f']
    },
    "湖北": {
        "武汉": ['g', 'h', 'i'],
        "黄石": ['j', 'k', 'l']
    }
}
while True:
    province = input("请输入要查询的省份")
    for i in dic:
        if province == i:
            for j in dic[i]:
                print(j)
            city = input("请选择城市")
            for j in dic[i]:
                if j == city:
                    for k in dic[i][j]:
                        print(k)
            break
        elif province != i:
            print("未查询到该城市")
            break


