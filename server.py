from bottle import run
from httprpc.bottle_api import api, register_auth_func


def auth_func(username, password):
    return username == password


register_auth_func(auth_func)


@api()
def hello(a, b):
    return a + b


@api('/demo')
def hello(a, b):
    return a + b


run(host='localhost', port=8000, reloader=True)
