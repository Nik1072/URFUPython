def fast_exponentiation_algorithm(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponentiation_algorithm(a ** 2, n // 2)
    if n % 2 != 0:
        return a * fast_exponentiation_algorithm(a, n - 1)

input_number = int(input())
n = int(input())
print(fast_exponentiation_algorithm(input_number, n))