def memoized(func):
    func_name = func.__name__
    func_doc = func.__doc__
    cache = {}

    def wrapper(*args):
        if args[0] in cache.keys():
            result = cache[args[0]]
        else:
            result = func(args[0])
            cache[args[0]] = result
        return result
    return wrapper


@memoized
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)