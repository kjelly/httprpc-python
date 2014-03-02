from bottle import post, request
from httprpc.packer import load, load_from_json
import json
import copy


auth_func = None


def register_auth_func(func):
    global auth_func
    auth_func = func


def load_from_forms(forms_dict):
    return load_from_json(forms_dict['data'][0])


def api(prefix='/', auth=None):
    def func_wrapper(func):
        if prefix[-1] == '/':
            path = prefix + func.__name__
        else:
            path = prefix + '/' + func.__name__

        @post(path)
        def inner():
            forms = copy.deepcopy(request.forms.dict)
            if auth_func:
                if not auth_func(forms.get('username', ''),
                                 forms.get('password', '')):
                        return {'error': 'auth failed'}
            args, kwargs = load_from_forms(forms)
            try:
                return {'ret': func(*args, **kwargs)}
            except Exception as e:
                return {'error': str(e)}
        return inner
    return func_wrapper
