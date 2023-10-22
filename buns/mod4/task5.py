stats = []
symbol_in_stats_Id = 0

the_path_to_the_file = str(input('Введите полный путь до файла в котором будем подсчитывать статистику '))
file_open = open(the_path_to_the_file, 'r', encoding='utf-8')
file_data = file_open.read()
file_data = list(file_data)
copy_file_data = file_data[:]
for symbol_of_file_data in file_data:
    if symbol_of_file_data.isalpha() and copy_file_data.count(symbol_of_file_data) != 0:
        stats.append([symbol_of_file_data, copy_file_data.count(symbol_of_file_data)])
        for _ in range(copy_file_data.count(symbol_of_file_data)):
            copy_file_data.remove(symbol_of_file_data)
file_open.close()

stats.sort(key = lambda x: x[1])

the_path_to_the_endfile = str(input('Введите полный путь для предполагаемого файла, в который мы выведем статистику (программа сама создаст файл по данным пути) '))

endfile_file = open(the_path_to_the_endfile, "w+")
for stats_of_one_symbol in stats:
    for _ in stats_of_one_symbol:
        endfile_file.write(str(_))
        endfile_file.write(' ')
    endfile_file.write('\n')

endfile_file.close()
