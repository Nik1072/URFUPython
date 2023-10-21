# Параметры ввода: в программу мы получим строку в виде '<число> <число> <число>...')
input_data = str(input())

all_list = input_data.split()
list_of_numbers = []
for word in all_list:
    if word.isnumeric():
        list_of_numbers.append(int(word))
print(list_of_numbers)

equal_numbers_exist = False
for _ in list_of_numbers:
    if list_of_numbers.count(_) > 1:
        if list_of_numbers.count(_) == len(list_of_numbers):
            print('Все числа равны')
            equal_numbers_exist = True
            break
        else:
            print('Есть равные и неравные числа')
            equal_numbers_exist = True
            break
if equal_numbers_exist == False:
    print('Все числа разные')


