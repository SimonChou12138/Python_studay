# 1.  30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
people = {}
for x in range(1, 31):
    people[x] = 1
# print(people)
check = 0
i = 1
j = 0
while i <= 31:
    if i == 31:
        i = 1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i += 1
            continue
        else:
            check += 1
            if check == 9:
                people[i] = 0
                check = 0
                print("{}号下船了".format(i))
                j += 1
            else:
                i += 1
                continue

# 2.使用 time 模块来实现秒表功能：
import time
print("请按下回车开始计时，按下ctrl+c结束计时")
startTime = time.time()
while True:
    try:
        input()
        print("开始")
        while True:
            print('计时: ', round(time.time() - startTime, 0), '秒', end="\r")
            time.sleep(1)

    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - startTime, 2), 'secs')
        break
