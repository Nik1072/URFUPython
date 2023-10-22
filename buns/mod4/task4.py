input_data = input()
input_data_list = list(input_data)
copy_data_list = input_data_list[:]
equal_symbols = []
id_equal_symbol = 0
palindrome_exists = False
palindrome = []
palindrome_str = ''

for symbol in input_data_list:
    while copy_data_list.count(symbol) >= 2:
        equal_symbols.append(symbol)
        copy_data_list.remove(symbol)
        copy_data_list.remove(symbol)

if len(input_data_list) % 2 == 0:
    if len(copy_data_list) == 0:
        palindrome_exists = True
else:
    if len(copy_data_list) == 1:
        palindrome_exists = True

if palindrome_exists:
    palindrome.extend(equal_symbols)
    if len(copy_data_list) == 1:
        palindrome.extend(copy_data_list)
    palindrome.extend(reversed(equal_symbols))

for _ in palindrome:
    palindrome_str += _

print(palindrome_str)
