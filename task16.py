"""
Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного аргумента x.
Напишите программу, которая вычисляет значение этой функции для n чисел.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода на тесте.

Формат ввода:
На первой строке находится число n − количество значений, на которых нужно посчитать функцию. После этого следует n строк, на каждой строке по одному целому числу.

Формат вывода:
n строк, в каждой из которой результат вычисления функции на соответствующем аргументе.
"""

def f(x):
    return x*x + x


numbers = []
result_cache = dict()

for i in range(int(input())):
    numbers.append(int(input()))

for num in numbers:
    if result_cache.get(num) is None:
        result = f(num)
        result_cache[num] = result
        print(result)
    else:
        print(result_cache[num])
