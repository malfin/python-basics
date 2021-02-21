import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # до
        value = func(*args, **kwargs)
        # после
        return value

    return wrapper_decorator
