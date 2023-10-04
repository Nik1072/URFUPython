start_str = input()
vowel = 0
consonant = 0
for symbol in start_str:
    if (symbol != ' ') and (symbol != 'ь') and (symbol != 'ъ'):
        if (symbol == 'а') or (symbol == 'у') or (symbol == 'о') or (symbol == 'и') or (symbol == 'э') or (symbol == 'ы') or (symbol == 'я') or (symbol == 'ю') or (symbol == 'е') or (symbol == 'ё'):
            vowel += 1
        else:
            consonant += 1
print(vowel, consonant)
