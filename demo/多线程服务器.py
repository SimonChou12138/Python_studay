from socket import *
from threading import Thread

def moreMis(newSocket,destInfo):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('recv[%s]:%s' % (str(destInfo), recvData))
        else:
            print("[%s]客户端已关闭"%str(destInfo))
            break
    newSocket.close()

#服务器主线程
def main():
    serSocket = socket(AF_INET,SOCK_STREAM)#创建新的套接字
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#重复使用绑定的信息
    localAdd=('',6080)
    serSocket.bind(localAdd)#绑定端口
    serSocket.listen(5)#最大接收数

    try:
        while True:
            print("等待新的客户端到来")
            newSocket,destInfo=serSocket.accept()
            T_New=Thread(target=moreMis(),args=(newSocket,destInfo))
            T_New.start
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()