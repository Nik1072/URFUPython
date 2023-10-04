def translation(to_convert, base):
    if base < 2 or base > 36:
        return ''
    final_value = ''
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while to_convert > 0:
        final_value = alphabet[to_convert % base] + final_value
        to_convert = to_convert // base
    return final_value

try:
    input_data = int(input())
except ValueError:
    print("Неверный ввод")
    exit()

if input_data <= 0:
    print("Неверный ввод")
    exit()

print(translation(input_data, 2))
print(translation(input_data, 8))
print(translation(input_data, 16))
