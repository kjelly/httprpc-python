from httprpc.client import Client

a = Client("http://127.0.0.1:8000", username='a', password='a')
print a.hello(a=1, b=1)
print a.demo.hello(a=1, b=1)
