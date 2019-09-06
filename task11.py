"""
Напишите программу, которая находит все позиции вхождения подстроки в строку.

Формат ввода:
На первой строке содержится исходная строка, на второй строке ввода указана подстрока, позиции которой требуется найти.
Строки состоят из символов латинского алфавита.

Формат вывода:
Строка, содержащая индексы (индексация начинается с нуля) вхождения подстроки в строку,
разделённые пробелом или число -1 в случае, когда подстрока не найдена.
"""


def find_all(st, substring):
    start_position = 0
    indexes = []
    while True:
        start_position = st.find(substring, start_position)
        if start_position == -1:
            return indexes
        indexes.append(start_position)
        start_position += 1


st = input()
substring = input()

result = list(find_all(st, substring))

if len(result) == 0:
    print("-1")
else:
    for num in result:
        print(num, end=" ")

# print(list(find_all(st, substring)))