# 一. 判断字符串是否是全部小写
import re
str = "simon chou is very excellen tman"
temp = re.match('^[a-z]+', str)
if temp:
    print("Ture")
else:
    print("False")

# 二.  首字母缩写词扩充
def expand_abbr(sen, abbr):
    lenabbr = len(abbr)
    ma = ''
    for i in range(0, lenabbr-1):
        ma += abbr[i] + "[a-z]+" + ' ' + '([a-z]+ )?'
    ma += abbr[lenabbr-1] + "[a-z]+"
    print("ma:", ma)
    ma = ma.strip(' ')
    p = re.search(ma, sen)
    if p:
        return p.group()
    else:
        return ""


print(expand_abbr("Welcome to Algriculture Bank of China", 'ABC'))

# 三. 去掉数字中的逗号
sen = "abc,123,456,789,mnp"
while 1:
    mm = re.search("\d,\d", sen)
    if mm:
        mm = mm.group()
        sen = sen.replace(mm, mm.replace(",", ""))
        print(sen)
    else:
        break

# 四. 中文处理之年份转换（例如：一九四九年--->1949年）
import re
m0 =  "在一九四九年新中国成立"
m1 =  "比一九九零年低百分之五点二"
m2 =  '人一九九六年击败俄军,取得实质独立'

def fuc(m):
    a = re.findall("[零|一|二|三|四|五|六|七|八|九]+年", m)
    if a:
        for key in a:
            print(key)
    else:
        print("NULL")

fuc(m0)
fuc(m1)
fuc(m2)
