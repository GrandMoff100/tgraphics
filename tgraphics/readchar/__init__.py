from .readchar import readkey
from . import key


def wait_for_key():
    k = readkey()
    keys = {getattr(key,attr):attr for attr in dir(key) if not attr.startswith('_')}
    if k in 'qwertyuiopasdfghjklzxcvbnm':
        return k
    elif k in keys:
        return keys[k]
    return k
    


