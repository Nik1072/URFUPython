the_path_to_the_file = str(input('Введите полный путь до файла в котором будем подсчитывать статистику по буквам '))

str_open = open(the_path_to_the_file, 'r')
list_file = str_open.read()
count_dict = {}
count_letter = 0
for letter in list_file:
    if (letter.isalpha()):
        x = count_dict.get(letter, 0)
        count_dict[letter] = x + 1
        count_letter += 1
count_letter_dict = [(k, "{:8.6f}".format(count_dict[k] / count_letter)) for k in count_dict.keys()]
str_open.close()
count_letter_dict.sort(key=lambda x: x[1], reverse=True)
print()

the_path_to_the_endfile = str(input('Введите полный путь до файла в который занесём статистику '))
my_file = open(the_path_to_the_endfile, "w+")
for i in count_letter_dict:
    my_file.write(i[0] + " " + i[1] + ' * 100%')
    my_file.write('\n')
    print(i[0] + " " + i[1] + ' * 100%')
my_file.close()