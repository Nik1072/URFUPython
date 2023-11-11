import time


def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return 'Not enough arguments'
        elif len(args) > 1:
            return 'Too many arguments'
        elif type(args[0]) is not int:
            return 'Wrong types'
        elif args[0] < 0:
            return 'Negative argument'
        return func(*args)
    return wrapper


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


def timer(func):
    def wrapper(n, *args, **kwargs):
        if not hasattr(wrapper, 'start_time'):
            wrapper.start_time = time.time()

        result = func(n, *args, **kwargs)

        if not hasattr(wrapper, 'execution_time'):
            wrapper.execution_time = time.time() - wrapper.start_time
            return f"Результат: {result}, Время выполнения: {wrapper.execution_time} секунд"
        else:
            return result

    return wrapper


# timer применен только к test_fibonacci_with_memoized
# (и test_fibonacci_without_memoized), а не к оригинальной,
# функции, чтобы избежать множественного измерения времени
# при рекурсивных вызовах. По этой же причине пришлось
# глянуть курс немного дальше по темам (отсюда hasattr),
# ибо выполненный на паре декоратор timer не дружит с
# рекурсивными функциями (опять же, из-за множественного
# вызова)

@timer
def test_fibonacci_with_memoized(n):
    return fibonacci_with_memoized(n)


@timer
def test_fibonacci_without_memoized(n):
    return fibonacci_without_memoized(n)


@validate_args
@memoized
def fibonacci_with_memoized(n):
    if n < 2:
        return n
    return fibonacci_with_memoized(n - 1) + fibonacci_with_memoized(n - 2)


@validate_args
def fibonacci_without_memoized(n):
    if n < 2:
        return n
    return fibonacci_without_memoized(n - 1) + fibonacci_without_memoized(n - 2)


print(f"Тест функции с декоратором memoized:\n{test_fibonacci_with_memoized(31)}\n\nТест функции без декоратора memoized:\n{test_fibonacci_without_memoized(31)}")

