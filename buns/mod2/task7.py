data = str(input())
zero_count = 0
ones_count = 0

for i in data:
    if i == '0':
        zero_count += 1
    if i == '1':
        ones_count += 1

if zero_count == ones_count:
    print("yes")
else:
    print("no")