def recursive_Euclidean_algorithm(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return recursive_Euclidean_algorithm(a % b, b)
        else:
            return recursive_Euclidean_algorithm(a, b % a)

first_number = int(input('Введите первое число '))
second_number = int(input('Введите второе число '))
greatest_common_divisor = recursive_Euclidean_algorithm(first_number, second_number)
print('НОД', first_number, 'и', second_number, '=', greatest_common_divisor)