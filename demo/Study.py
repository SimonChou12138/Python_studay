'''

classmates = ['a','b','c']
print(classmates)
print(len(classmates))

for x in classmates:
    print(x)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

d={'a':1,'b':2,'c':3}
print(d['a'])
d['d']=4
print(d['d'])
d['a']=5
print(d['a'])
print('a' in d)
d.pop('d')
print(d.get('d'))

s=set([1,2,3])
print(s)
t=(1,2,3)
t2=(1,[2,3])
d={t,t2}
print(d)
s=set(t,t2)
print(s)
'''
'''
h = {(1,[2,3]):1} #报错
print(h[(1,[2,3])])
'''
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1= count()
f1()
f2()
f3()
'''
'''class student(object):
def __init__ (self,name,score):
    self.name=name
    self.score=score

Simon=student('SimonChou',100)
'''
# for i in range(100):
#     print(i)

# class  Test(object):
#     def __init__(self):
#         self.__num=100;
#
#     @property
#     def num(self):
#         print("---get---")
#         return self.__num
#
#     @num.setter
#     def num(self,newNum):
#         print("---set---",newNum)
#         self.__num=newNum;
# t=Test()
# t.num=200
# print(t.num)

# def Test(number):
#
#     print("---1---")
#
#     def test_in(number2):
#         print("---2---")
#         print(number+number2)
#
#     print("-0-0-")
#     return test_in
#
# T=Test(100)
# T(100)
# T(200)
# def Test(fun):
#
#     def inner():
#         print("--1--")
#         fun()
#
#     return inner
#
# @Test
# def f1():
#     print("--zms--")
#
# @Test
# def f2():
#     print("--zwy--")
#
# f1()
# f2()


# def Test(pre=""):
#
#     def Test_Up(fun):
#         def Test_in(*args,**kwargs):
#             print(*args,**kwargs)
#         return Test_in
#
#     return Test_Up
#
# @Test("Simon")
# def T1():
#     print("-"*30)
#
# T1(11,22,33)

# import types
# class Test():
#     def __init__(self,newName,newAge):
#         self.name=newName
#         self.age=newAge
#
# def run(self):
#     print("==%s"%self.name)
#
# test=Test("Simom",18)
# test.run=types.MethodType(run,test)
# test.run()
'''
def foi():
    n=0
    a,b=0,1
    while(n<10):
        print(b)
        c=a+b
        a=b
        b=c
        n+=1
foi()
'''
# def createNum():
#     a,b=0,1
#     for x in range(5):
#         yield (b)
#         a,b=b,a+b
#
# a=createNum()
# def test1():
#     while True:
#         print("--1--")
#         yield None
# def test2():
#     while True:
#         print("--2--")
#         yield None
#
# t1=test1()
# t2=test2()
# while True:
#     t1.__next__()
#     t2.__next__()
'''
# class Test(object):
#     def __init__(self,func):
#         print("--初始化")
#         print("func name is %s"%func.__name__)
#         self.__func=func
#     def __call__(self):
#         print("装饰器的功能")
#         self.__func()
# 
# # @Test
# def test():
#     print("--1--")
# Test(test)
'''
# class Person(object):
#     print("111")
#     def __init__(self):
#         self.name="abc"
'''
def Test(self):
    print("--Test---")

test1=type("test1",(),{"Test":Test})
t1=test1()
t1.Test()
'''
'''
# def upper_attr(future_class_name,future_class_parents,future_class_attr):
#     newAttr={}
#     for key,value in future_class_attr.items():
#         if not key.startswith("__"):
#             newAttr[key.lower()]=value
#     return type(future_class_name,future_class_parents,newAttr)
# 
# class Foo(object,metaclass=upper_attr):
#     bar="Simon"
# 
# f=Foo()
# print(f.bar)
'''
'''
import os
import time
ret=os.fork()
if ret==0:
    while True:
        print("---1---")
        time.sleep(1)
else:
    while True:
        print("---2---")
        time.sleep(1)
'''
'''
from multiprocessing import Process
import time
import random

def test():
    for i in range(5):
        print("---%d---"%i)
        time.sleep(1)


if __name__=='__main__':
    p = Process(target=test)
    p.start()

# while True:
#     print("---main---")
#     time.sleep(1)
'''
'''
from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print("--1--")
            time.sleep(1)

if __name__=='__main__':
    p=MyNewProcess()
    p.start()

    while True:
        print("--main--")
        time.sleep(1)
'''
'''
from multiprocessing import Pool
import os
import random
import time

def worker(num):
    for i in range(5):
        print("==pid==%d==num==%d"%(os.getpid(),num))
        time.sleep(1)

if __name__ == '__main__':
    pool=Pool(3)

    for i in range(10):
        print("==%d=="%i)
        pool.apply_async(worker,(i,))

    pool.close()
    pool.join()
'''
'''
from threading import Thread
import time

def test():
    print("--啦啦啦--")

if __name__=='__main__':
    for x in range(5):
        t=Thread(target=test)
        t.start()
'''

# import threading
# import time
#
# class Test(threading.Thread):
#     def run(self):
#         for x in range(5):
#             print("%d--"%x+self.name)
#
# if __name__=='__main__':
#     t=Test()
#     t.start()
'''
from threading import Thread,Lock

g_num=0

def Test1():
    global g_num
    lock.acquire()
    for x in range(1000000):
        g_num+=1
    lock.release()
    print("---1---：",g_num)

def Test2():
    global g_num
    lock.acquire()
    for x in range(1000000):
        g_num+=1
    lock.release()
    print("---2---：",g_num)

if __name__== '__main__':
    lock=Lock()
    t=Thread(target=Test1)
    t.start()

    t = Thread(target=Test2)
    t.start()
'''
'''
from threading import Thread,Lock

class Test1(Thread):
    def run(self):
        if lock1.acquire():
            print("--Test1--")
            lock2.release()

class Test2(Thread):
    def run(self):
        if lock2.acquire():
            print("--Test2--")
            lock3.release()

class Test3(Thread):
    def run(self):
        if lock3.acquire():
            print("--Test3--")
            lock1.release()

if __name__=='__main__':
    lock1=Lock()
    lock2=Lock()
    lock2.acquire()
    
    lock3=Lock()
    lock3.acquire()

    t=Test1()
    t.start()
    t = Test2()
    t.start()
    t = Test3()
    t.start()
'''
'''
#生产者消费者模型
import threading
from queue import Queue
import time

class Producer(threading.Thread):
    def run(self):
        global queue
        count=0
        if queue.qsize()<=10:
            for i in range(10):
                count+=1
                msg="生产了商品:"+str(count)
                queue.put(msg)
                print(msg)
        time.sleep(0.5)

class Customer(threading.Thread):
    def run(self):
        global queue
        if queue.qsize()>=10:
            for i in range(2):
                msg=self.name+"消费了--"+queue.get()
                print(msg)
        time.sleep(1)


if __name__=='__main__':
    queue=Queue()

    for i in range(10):
        queue.put('初始化商品'+str(i))

    for i in range(2):
        p=Producer()
        p.start()

    for i in range(5):
        c=Customer()
        c.start()
'''
'''
from socket import *
#TCP服务器
tcpSerSocket=socket(AF_INET,SOCK_STREAM)#创建套接字
tcpSerSocket.bind("",6080)#绑定端口
tcpSerSocket.listen(5) #服务器最大的接收数，变成被动套接字
clientSocket,clientInfo=tcpSerSocket.accept()  #等待客户端链接（新客户端，新客户端IP | port）

recvData=clientSocket.recv(1024) #缓冲区每次接收1024字节
print("%s:%s"%(str(clientInfo),recvData))

clientSocket.close()
tcpSerSocket.close()
'''
'''
#TCP客户端
from socket import *
clientSocket=socket(AF_INET,SOCK_STREAM)#创建套接字
clientSocket.connect(("192.168.123.123",6080))

#注意：
#1.tcp客户端已经链接好了服务器，所以在以后的数据发送中，不需要填写对方的ip和port
#2.udp在发送数据的时候，因为没有之前的链接，所以需要在每次发送中都要填写接收方的ipport————》类似写信
clientSocket.sent("haha".encode("gb2312"))

recvData=clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()

'''
'''
import time
#算法引入
start_time=time.time()#开始时间
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a+b+c==1000 and a**2+b**2==c**2:
                print("a:%d--b:%d--c:%d"%(a,b,c))
end_time=time.time()#结束时间
print("耗时：%d"%(end_time-start_time))
'''
'''
import time
#升级算法
start_time=time.time()
for a in range(1000):
    for b in range(1000):
        c=1000-a-b
        if a**2+b**2==c**2:
            print("a:%d--b:%d--c:%d" % (a, b, c))
end_time=time.time()
print("耗时：%d"%(end_time-start_time))
'''
'''
# list时间效率测试
# coding :utf-8

from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += [i]
        # 在python中+=效率与li=li+[i]不一样


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


def test5():
    li=[]
    for i in range(10000):
        li.extend([i])

def t6():
    li = []
    for i in range(10000):
        li.append(i)


def t7():
    li=[]
    for i in range(10000):
        li.insert(0,i)


timer1 = Timer("test1()", "from __main__ import test1")
print("append:", timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2")
print("+:", timer2.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3")
print("li[]:", timer3.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4")
print("list:", timer4.timeit(1000))

timer5 = Timer("test5()", "from __main__ import test5")
print("extend:", timer5.timeit(1000))

timer6 = Timer("t6()", "from __main__ import t6")
print("list:", timer6.timeit(1000))

timer7 = Timer("t7()", "from __main__ import t7")
print("extend:", timer7.timeit(1000))
'''
