data = input()
count = 0
sum_even_numbers = 0
sum_odd_numbers = 0
for symbol_of_data in data:
    count += 1
    if (count % 2) != 0:
        sum_odd_numbers += int(symbol_of_data)
    else:
        sum_even_numbers += int(symbol_of_data)
if ((sum_odd_numbers + 3 * sum_even_numbers) % 10 == 0):
    print('yes')
else:
    print('no')
