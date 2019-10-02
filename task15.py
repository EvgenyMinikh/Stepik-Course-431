"""
Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Формат ввода:
Одна строка с целыми числами, разделёнными пробелом.

Формат вывода:
Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.
"""

inp = input()
input_numbers = [int(i) for i in inp.split()]

num_dict = dict()
for num in input_numbers:
    if num_dict.get(num) is None:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

for key in num_dict.keys():
    if num_dict[key] > 1:
        print(key, end=' ')