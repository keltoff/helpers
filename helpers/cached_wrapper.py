

def cached(func):
    cache = dict()

    def wrapper(*args, **kwargs):
        key = args[0]
        if key == 'reset':
            cache.clear()
            return None
        elif key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper
