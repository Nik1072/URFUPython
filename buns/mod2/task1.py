data = input()
first_number = ''
second_number = ''
current_value = ''
first_number_received = False

for symbol_of_data in data:
    if first_number_received == False:
        if symbol_of_data == ',':
            first_number_received = True
            first_number = current_value
            current_value = ''
        else:
            current_value += symbol_of_data
    else:
        if symbol_of_data != ' ':
            second_number += symbol_of_data

first_number = int(first_number)
second_number = int(second_number)

print(first_number % second_number)
