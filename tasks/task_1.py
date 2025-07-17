from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_list = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        print(f"Вызов: {func.__name__}({', '.join(arg_list)})")

        result = func(*args, **kwargs)

        print(f"Результат: {result}")

        return result
    return wrapper
