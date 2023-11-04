def armstrong_numbers_generator():
    number = 1
    while True:
        digits_in_number = [int(x) for x in str(number)]
        num_digits = len(digits_in_number)
        sum_of_powers = sum([x ** num_digits for x in digits_in_number])
        if sum_of_powers == number and number not in range(1, 10):
            yield number
        number += 1


a_n_gen = armstrong_numbers_generator()


def get_armstrong_numbers():
    return next(a_n_gen)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')

# Ожидаемый результат кода:
# 153 370 371 407 1634 8208 9474 54748
