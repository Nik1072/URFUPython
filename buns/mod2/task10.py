start_str = input()
end_str = ''
before_symbol = ''
for symbol in start_str:
    if (symbol == ' '):
        end_str += before_symbol
        before_symbol = ''
    else:
        before_symbol = symbol
if before_symbol != ' ':
    end_str += before_symbol
    before_symbol = ''
print(end_str)