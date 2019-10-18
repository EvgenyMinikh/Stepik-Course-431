"""
Напишите программу, которая выводит число в стиле LCD калькулятора.
На вход программе подаётся последовательность цифр, которую нужно вывести на экран в специальном стиле (см. пример).
Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе должен быть один пустой столбец.
Перед первой цифрой не должно быть пробелов.
Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ x ("икс"),
горизонтальная линия создаётся из символа - ("дефис"), а вертикальная -- из символа вертикальной черты: |
"""


def draw_border():
    print("x", end="")
    for i in range(len(num)):
        print("-----", end="")
    print("x")


d = {'0': (' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '),
     '1': ('    ', '   |', '   |', '    ', '   |', '   |', '    '),
     '2': (' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- '),
     '3': (' -- ', '   |', '   |', ' -- ', '   |', '   |', ' -- '),
     '4': ('    ', '|  |', '|  |', ' -- ', '   |', '   |', '    '),
     '5': (' -- ', '|   ', '|   ', ' -- ', '   |', '   |', ' -- '),
     '6': (' -- ', '|   ', '|   ', ' -- ', '|  |', '|  |', ' -- '),
     '7': (' -- ', '   |', '   |', '    ', '   |', '   |', '    '),
     '8': (' -- ', '|  |', '|  |', ' -- ', '|  |', '|  |', ' -- '),
     '9': (' -- ', '|  |', '|  |', ' -- ', '   |', '   |', ' -- ')
     }

number_height = 7

num = input()
draw_border()

for i in range(number_height):
    print("|", end="")

    for ch in num:
        print(d[ch][i], end=" ")

    print("|")

draw_border()
