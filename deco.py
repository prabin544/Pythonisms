from functools import wraps

def hello_goodbye_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Hello, Goodbye "{orig_val}"'
    return wrapper

@hello_goodbye_decorator
def decorate(text):
    return text