# coding:utf-8

import time

# from MyWebServer import HTTPServer
HTML_ROOT_DIR = "./"

class Application(object):
    """框架的核心部分=框架的主题程序，通用框架"""
    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        # 获取路径名字
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            # 访问静态文件
            file_name = path[7:]
            # 打开文件，读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 代表未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "Not Found"
            else:
                file_data = file.read()
                file.close()

                status = "200 Ok"
                headers = []
                start_response(status, headers)
                return file_data.decode("UTF-8")

        for url, handler in self.urls:
            # 判断路径名字是否在路由信息里包括
            if path == url:
                return handler(env, start_response)

        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "Not Found"


def show_time(env, start_response):
    status = "200 ok"
    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)

    return time.ctime()


def say_hello(env, start_response):
    status = "200 ok"
    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)

    return "Hello Simon"


urls = [
            ("/", show_time),
            ("/ctime", show_time),
            ("/sayhello", say_hello)
        ]

app = Application(urls)


# if __name__ == "__main__":
#
#     urls = [
#             ("/", show_time),
#             ("/ctime", show_time),
#             ("/sayhello", say_hello)
#         ]
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
