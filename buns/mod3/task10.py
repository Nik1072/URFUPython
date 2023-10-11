matrix_side = int(input())
for first_num in range(1, matrix_side + 1):
    for second_num in range(1, matrix_side + 1):
        if second_num != matrix_side:
            print(second_num, end=', ')
        else:
            print(second_num)

print()

for first_num in range(1, matrix_side + 1):
    for second_num in range(1, matrix_side + 1):
        if second_num != matrix_side:
            print(first_num, end=', ')
        else:
            print(first_num)