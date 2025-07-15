def simple_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Из кэша")
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper
