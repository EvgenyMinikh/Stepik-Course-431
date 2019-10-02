"""
Последовательность n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей последовательных
элементов принимают все возможные значения между 1 и n−1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как абсолютные разности
равны 4 1 3 2, соответственно, а n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1≤n≤10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.
"""

from math import fabs

inp = input()

input_numbers = [int(i) for i in inp.split()]
if len(input_numbers) == 1:
    print("Jolly")
    exit(0)


jolly_pattern = [i for i in range(1, len(input_numbers))]
diff_lst = []

for i in range(len(input_numbers) - 1):
    first_num = input_numbers[i]
    second_num = input_numbers[i+1]
    diff = int(fabs(first_num - second_num))
    diff_lst.append(diff)

diff_lst.sort()
if diff_lst == jolly_pattern:
    print("Jolly")
else:
    print("Not jolly")
