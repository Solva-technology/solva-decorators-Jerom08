from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Все аргументы должны быть положительными")

        for value in kwargs.values():
            if isinstance(kwargs, (float, int)) and kwargs <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper
