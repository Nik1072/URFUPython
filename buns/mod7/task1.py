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

# Проверим на практике
@validate_args
def random_func(x):
    return x


r_f = random_func
# По условию должен быть передан ровно один аргумент. Рассмотрим варианты:

# Если передано меньшее количество:
result = r_f()
print('ТЕСТ 1:\nОжидаемый вывод: Not enough arguments\nПолученный ответ: {}'.format(result))

# Если передано больше аргументов:
result = r_f(1, 2)
print('ТЕСТ 2:\nОжидаемый вывод: Too many arguments\nПолученный ответ: {}'.format(result))

# Если аргумент не целое число:
result = r_f('1')
print('ТЕСТ 3:\nОжидаемый вывод: Wrong types\nПолученный ответ: {}'.format(result))

# Если аргумент отрицателен:
result = r_f(-1)
print('ТЕСТ 4:\nОжидаемый вывод: Negative argument\nПолученный ответ: {}'.format(result))

# Аргумент соответсвует всем условиям (переданная декоратору функция просто возвращает этот самый аргумент):
result = r_f(1)
print('ТЕСТ 5:\nОжидаемый вывод: 1\nПолученный ответ: {}'.format(result))



