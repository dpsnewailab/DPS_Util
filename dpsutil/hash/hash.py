import hashlib
import datetime


def hash(data, hash_func=hashlib.sha1) -> str:
    assert hasattr(hash_func, "__call__")
    return hash_func(data).hexdigest()


def short_hash(msg: (str, bytes)) -> str:
    assert isinstance(msg, (str, bytes))
    if type(msg) is str:
        msg = msg.encode("UTF-8")
    return hash(msg)[:10]


def hash_now() -> str:
    return short_hash(datetime.datetime.now().isoformat())


__all__ = ['hash_now', 'hash', 'short_hash']
