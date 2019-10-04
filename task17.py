"""
Напишите программу, которая шифрует текст шифром Цезаря.
Используемый алфавит − пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек записана зашифрованная последовательность.
"""

alphabet = ' abcdefghijklmnopqrstuvwxyz'
shift = int(input())
source_string = input().strip()
print('Result: "', end='')
for letter in source_string:
    position = alphabet.find(letter)
    new_position = (position + shift) % 27
    print(alphabet[new_position], end='')
print('"', end='')
