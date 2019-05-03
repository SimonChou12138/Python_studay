import time
import threading

def f0(a1, a2):
    #time.sleep(2)
    print(time.ctime())
    print(a1+a2)

t = threading.Thread(target=f0, args=(111, 222))
#t.setDaemon(True)
t.start()

# 假定这是我的银行存款
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# python多线程问题，模拟抢退票过程
