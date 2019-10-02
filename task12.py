'''
Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа n и m, количество строк и столбцов, соответственно.
Далее следуют n строк, содержащих по m целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести m строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.
'''

matrix_size = input()
rows, columns = matrix_size.split()
matrix = []

for i in range(int(rows)):
    line = input()
    matrix.append(line.split())

transponded_matrix = list(zip(*matrix))

for row in transponded_matrix:
    for item in row:
        print(item, end=' ')
    print('')
