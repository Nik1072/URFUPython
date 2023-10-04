numbers = input()
flag = False
position_of_check_number1_in_numbers = 0
position_of_check_number2_in_numbers = 0
for check_number1 in numbers:
    if flag == True:
        break
    position_of_check_number1_in_numbers += 1
    for check_number2 in (numbers):
        if flag == True:
            break
        position_of_check_number2_in_numbers += 1
        if position_of_check_number1_in_numbers != position_of_check_number2_in_numbers:
            if (check_number1 == check_number2) and (check_number1 != ' '):
                flag = True
                break
    position_of_check_number2_in_numbers = 0
print(flag)

# # or a simpler option:
# ...
# numbers = input()
# flag = False
# count_of_number_0 = 0
# count_of_number_1 = 0
# count_of_number_2 = 0
# count_of_number_3 = 0
# count_of_number_4 = 0
# count_of_number_5 = 0
# count_of_number_6 = 0
# count_of_number_7 = 0
# count_of_number_8 = 0
# count_of_number_9 = 0
# for check_number1 in numbers:
#     if check_number1 == '0':
#         count_of_number_0 += 1
#     if check_number1 == '1':
#         count_of_number_1 += 1
#     if check_number1 == '2':
#         count_of_number_2 += 1
#     if check_number1 == '3':
#         count_of_number_3 += 1
#     if check_number1 == '4':
#         count_of_number_4 += 1
#     if check_number1 == '5':
#         count_of_number_5 += 1
#     if check_number1 == '6':
#         count_of_number_6 += 1
#     if check_number1 == '7':
#         count_of_number_7 += 1
#     if check_number1 == '8':
#         count_of_number_8 += 1
#     if check_number1 == '9':
#         count_of_number_9 += 1
#     if ((count_of_number_0 == 2) or (count_of_number_1 == 2) or (count_of_number_2 == 2) or (count_of_number_3 == 2) or (count_of_number_4 == 2) or (count_of_number_5 == 2) or (count_of_number_6 == 2) or (count_of_number_7 == 2) or (count_of_number_8 == 2) or (count_of_number_9 == 2)):
#         flag = True
#         break
# print(flag)