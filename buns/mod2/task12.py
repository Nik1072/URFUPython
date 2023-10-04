start_number = input()
edit_number = ''
for part_of_number in start_number:
    if (part_of_number != '-') and (part_of_number != '(') and (part_of_number != ')') and (part_of_number != ' '):
        edit_number += part_of_number
print(edit_number)