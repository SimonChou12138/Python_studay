from socket import *
from threading import Thread
#模拟聊天室

def sentMsg():#发消息
    while True:
        sendData=input("<<")
        udpSocket.sendto(sendData.encode("GB2312"),(destIp,destPort))

def getMsg():#获取消息
    while True:
        recvData=udpSocket.recvfrom(1024)
        print("[%s]:%s",str(recvData[1]),recvData[0].encode("GB2312"))

udpSocket=None
destIp=""
destPort=0

def main():
    global udpSocket
    global destIp
    global destPort

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    destIp = input("请输入对方Ip")
    destPort = input("请输入对方的端口")

    udpSocket.bind(('',6080))

    T_Sent=Thread(target=sentMsg)
    T_Get=Thread(target=getMsg)

    T_Sent.start()
    T_Get.start()

    T_Sent.join()
    T_Get.join()


if __name__=='__main__':
    main()