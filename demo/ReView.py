# 静态web多进程服务器
# coding:utf-8
# import socket
# from multiprocessing import Process
#
# def handle_clinet(client_socket):
#     request_data = client_socket.recv(1024)
#     print("request data:", request_data)
#
#     responce_start_line = "HTTP/1.1 200 OK\r\n"
#     responce_headers = "Server: My server\r\n"
#     responce_body = "hello Simon"
#     responce = responce_start_line+responce_headers+"\r\n"+responce_body
#     print("responce data", responce)
#
#     client_socket.send(bytes(responce, "utf-8"))
#     client_socket.close()
#
#
# if __name__ == "__main__":
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(("", 8000))
#     server_socket.listen(128)
#
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print("[%s, %s]用户连上了"%(client_address[0], client_address[1]))
#
#         handle_clinet_process = Process(target=handle_clinet, args=(client_socket,))
#         handle_clinet_process.start()
#         client_socket.close()

# # 多线程服务器
# from socket import *
# import threading
#
# def handle(newSocket, newInfo):
#     while True:
#         recvData = newSocket.recv(1024)
#         if len(recvData) > 0 :
#             print("recv[%s]:[%s]" % (str(newInfo), recvData))
#         else:
#             print("没有发送信息,回话已结束")
#             break
#
# if __name__ == "__main__":
#     server_socket = socket(AF_INET, SOCK_STREAM)
#     server_socket.bind(('', 8000))
#     server_socket.listen(5)
#
#     while True:
#         newSocket, newInfo = server_socket.accept()
#         handle_thread = threading.Thread(target=handle, args=(newSocket, newInfo))
#         newSocket.close()

# 模拟聊天室
from socket import *
from threading import *

def sentMsg():
    while True:
        sentData = input("<<")
        udpScoket.sendto(sentData.encode("GB2312"), (destIp, destPort))

def getMsg():
    while True:
        recvData = udpScoket.recvfrom(1024)
        print("{0}:{1}".format(recvData[1], recvData[0].encode("GB2312")))

udpScoket = None
destIp = ""
destPort = 0

# if __name__ == "__main__":
#     global udpScoket
#     global destPort
#     global destIp
#
#     udpScoket = socket(AF_INET, SOCK_DGRAM)
#     destIp = input("请输入ip")
#     destPort = input("请输入端口")
#
#     udpScoket.bind(('', 1234))
#
#     threadSent = Thread(target=sentMsg)
#     threadGet = Thread(target=getMsg)
#
#     threadSent.start()
#     threadGet.start()
#
#     threadGet.join()
#     threadSent.join()

# 多进程复制文件夹
import os
from multiprocessing import *
import time


def copy(name, oldFileName, newFileName, queue):
    fr = open(oldFileName+"/"+name)
    fw = open(newFileName+"/"+name, "w")

    temp = fr.read()
    fw.write(temp)

    queue.put(name)
    fr.close()
    fw.close()


def main():
    oldFileName = input("请输入要复制的文件夹名字")
    newFileName = oldFileName + "--副件"
    os.mkdir(newFileName)

    fileName = os.listdir(oldFileName)
    p = Pool(5)
    queue = Manager().Queue()
    allNum = len(fileName)
    num = 0


    for name in fileName:
        p.apply_async(copy, args=(name, oldFileName, newFileName, queue))

    while True:
        queue.get()
        num += 1
        culum = num/allNum
        print("\r复制的进度是：%d%%" % (culum*100), end="")
        time.sleep(1)
        if num == allNum:
            break
    p.close()
    p.join()


if __name__ == "__main__":
    main()

