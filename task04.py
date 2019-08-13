"""
Напишите функцию f(x), принимающую дробное число x и возвращающую значение следующей функции, определённой на всей числовой прямой:
"""


def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2

    if x > 2:
        return 1 + (x - 2) ** 2

    return -x / 2

print(f(4.5))
