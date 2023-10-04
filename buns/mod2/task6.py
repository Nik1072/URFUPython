# Создадим необходимые переменные
domain = input() # Собственно само доменное имя
reversed_domain = ''
part_of_domain = ''

# Функция для переворота строки
def reversed(value):
    reverse_value = ''
    for i in range(len(value)-1,-1,-1):
        reverse_value += value[i]
    return reverse_value

reversed_domain = reversed(domain) # Перевернём доменное имя (для удобства последующего нахождения и вывода отдельных доменов, начиная с первого уровня)
for symbol_of_reversed_domain in reversed_domain: # Перебираем перевёрнутое доменное имя, собирая посимвольно
    if symbol_of_reversed_domain == '.': # При обноружении точки понимаем, что мы собрали отдельный домен
        part_of_domain = reversed(part_of_domain) # Переворачиваем его вновь в нормальный вид
        print(part_of_domain) # Выводим этот домен
        part_of_domain = '' # Чистим переменную, для следующего доменя
    else:
        part_of_domain += symbol_of_reversed_domain # Собираем посимвольно

# Дособираем, переворачиваем и выводим домен высшего уровня (он выпал из цикла, т.к. перевернув доменное имя, вышло так, что этот домен кончается не на точку, а с концом строки (а значит и цикла))
part_of_domain = reversed(part_of_domain)
print(part_of_domain)
art_of_domain = ''
