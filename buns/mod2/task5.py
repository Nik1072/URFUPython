alphabet = 'abcdefghijklmnopqrstuvwxyz'
start_symbol = ''
bias = ''
current_value = ''
position_of_start_symbol = 0
data_of_start_symbol_received = False
data = input()

for symbol_of_data in data:
    if data_of_start_symbol_received == False:
        if symbol_of_data == ',':
            data_of_start_symbol_received = True
            start_symbol = current_value
            current_value = ''
        else:
            current_value = symbol_of_data
    else:
        if symbol_of_data != ' ':
            current_value += symbol_of_data
bias = int(current_value)

for symbol_of_alphabet in alphabet:
    if symbol_of_alphabet == start_symbol:
        break
    else:
        position_of_start_symbol += 1

position_of_final_symbol = position_of_start_symbol + bias

while position_of_final_symbol < 0:
    position_of_final_symbol += 26
while position_of_final_symbol > 25:
    position_of_final_symbol -= 26

print(alphabet[position_of_final_symbol])