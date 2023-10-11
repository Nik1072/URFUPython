input_data = int(input())
print("Неверный ввод" if input_data < 0 else " ".join([bin(input_data)[2:], oct(input_data)[2:], hex(input_data)[2:]]))
