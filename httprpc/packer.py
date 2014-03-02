import json


def dump(args, kwargs):
    return {'args': args, 'kwargs': kwargs}


def dump_for_requests(args, kwargs):
    return {'data': json.dumps(dump(args, kwargs))}


def load(obj):
    return obj.get('args', []), obj.get('kwargs', {})


def load_from_json(json_data):
    obj = json.loads(json_data)
    return load(obj)
