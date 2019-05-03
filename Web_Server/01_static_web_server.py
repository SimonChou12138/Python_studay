# coding:utf-8
import socket

from multiprocessing import Process

# 常量
HTML_ROOT_DIR = ""


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:", request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello Simon"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)

    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端
    client_socket.close()


if __name__ == "__main__":
    # Tcp socket 服务器
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % (client_address[0], client_address[1]))
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
