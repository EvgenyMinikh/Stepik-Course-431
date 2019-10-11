"""
Напишите программу, которая выводит n первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).

Формат ввода:
Строка, содержащая одно целое число n, n>0.

Формат вывода:
Строка, содержащая требуемую последовательность чисел, разделённых пробелом.
"""


def printer(repeat, num):
    if num == 1:
        print(1)
        return

    global counter

    for i in range(repeat):
        print(repeat, end=' ')
        counter += 1
        if counter == num:
            break


num = int(input())
counter = 0

for i in range(num):
    printer(i, num)
    if counter == num:
        break
