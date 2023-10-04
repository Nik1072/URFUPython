data = input()
data_str = ''
symbol_at_the_beginning = ''
current_value = ''
count_of_symbol_at_the_beginning = 0
data_of_str_received = False

for symbol_of_data in data:
    if data_of_str_received == False:
        if symbol_of_data == ',':
            data_of_str_received = True
            data_str = current_value
            current_value = ''
        else:
            current_value += symbol_of_data
    else:
        if symbol_of_data != ' ':
            symbol_at_the_beginning = symbol_of_data

for symbol_of_data_str in data_str:
    if symbol_of_data_str == symbol_at_the_beginning:
        count_of_symbol_at_the_beginning += 1
    else:
        break
print(count_of_symbol_at_the_beginning)

