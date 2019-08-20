"""
Вы решили написать преобразователь кода на Python в код на Java. Так как на Java принят стандарт наименования CamelCase,
то вы решили научиться преобразовывать имена из underscore в этот формат. Для начала напишите программу,
которая переводит имена переменных из стиля написания underscore в стиль UpperCamelCase. Стиль underscore характеризуется тем,
что слова в имени пишутся маленькими буквами и разделяются между собой символом подчёркивания "_".
Стиль UpperCamelCase означает, что каждое слово пишется с большой буквы и разделителей между словами нет.
"""

word = input()
word_chars = list(word)
result = list()

result.append(word_chars[0].upper())

for index in range(1, len(word_chars)):
    if word_chars[index] == "_":
        continue

    if word_chars[index - 1] == "_":
        result.append(word_chars[index].upper())
    else:
        result.append(word_chars[index])

print("".join(result))