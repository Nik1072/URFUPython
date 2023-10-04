string = input()
a, b, c = '', '', ''
selected_value = ''
count = 1

for i in string:
    if i != ' ':
        selected_value += i
    else:
        if selected_value:
            if count == 1:
                a = int(selected_value)
            elif count == 2:
                b = int(selected_value)
            elif count == 3:
                c = int(selected_value)
            count += 1
            selected_value = ''
            
if count == 3:
    c = int(selected_value)
if (a > 1000 or b > 1000 or c > 1000) and (a < -1000 or b < -1000 or c < -1000):
    print('Неверный ввод')
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    
print(b)
