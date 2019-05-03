# coding:utf-8


def application(env, start_response):
    status = "200 ok"

    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status,headers)

    return "Hello World"
