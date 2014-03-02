import requests
from .packer import dump_for_requests


class Client(object):
    def __init__(self, uri, username='', password='', add_slash=False):
        self.uri = uri
        self.add_slash = add_slash
        self.username = username
        self.password = password

    def __getattr__(self, name):
        if name not in dir(object):
            if self.uri[-1] == '/':
                uri = self.uri + name
            else:
                uri = self.uri + '/' + name
            return Client(uri, username=self.username,
                          password=self.password, add_slash=self.add_slash)
        return super(Client, self).__getattr__(name)

    def __call__(self, *args, **kwargs):
        if self.add_slash and self.uri[-1] != '/':
            uri = self.uri + '/'
        else:
            uri = self.uri
        data = dump_for_requests(args, kwargs)
        data['username'] = self.username
        data['password'] = self.password
        r = requests.post(uri, data=data)
        result = r.json()
        if 'ret' in result:
            ret = result['ret']
        else:
            raise Exception(result.get('error', 'error'))

        return ret
