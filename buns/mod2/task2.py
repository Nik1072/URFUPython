square_side = float(input())

square_perimeter = round((square_side * 4), 2)
square_area = round((square_side ** 2), 2)
square_diagonal = round(square_side * (2 ** 0.5), 2)

print(square_perimeter, square_area, square_diagonal)