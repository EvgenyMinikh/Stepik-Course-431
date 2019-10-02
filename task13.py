"""
Поле для игры сапёр представляет собой сетку размером n×m. В ячейке сетки может находиться или отсутствовать мина.

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин,
находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится описание поля в виде
последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
n строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), при этом число
означает количество мин в соседних ячейках поля.
"""


class Cell:

    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.max_x = len(field[y]) - 1
        self.max_y = len(field) - 1
        self.cell_type = '-'
        self.cell_type = Cell.define_cell_type(self)

    def define_cell_type(self):

        if self.y == 0:
            self.cell_type += 'Top'

        if self.y == self.max_y:
            self.cell_type += 'Bottom'

        if self.x == 0:
            self.cell_type += 'Left'

        if self.x == self.max_x:
            self.cell_type += 'Right'

        return self.cell_type

    def calculate_neighbours(self):
        counter = 0
        start_x = self.x
        start_y = self.y
        stop_x = self.x
        stop_y = self.y

        if self.cell_type == '-TopLeft':
            start_x = self.x
            start_y = self.y
            stop_x = self.x + 1
            stop_y = self.y + 1

        if self.cell_type == '-TopRight':
            start_x = self.x - 1
            start_y = self.y
            stop_x = self.x
            stop_y = self.y + 1

        if self.cell_type == '-BottomRight':
            start_x = self.x - 1
            start_y = self.y - 1
            stop_x = self.x
            stop_y = self.y

        if self.cell_type == '-BottomLeft':
            start_x = self.x
            start_y = self.y - 1
            stop_x = self.x + 1
            stop_y = self.y

        if self.cell_type == '-':
            start_x = self.x - 1
            start_y = self.y - 1
            stop_x = self.x + 1
            stop_y = self.y + 1

        if self.cell_type == '-Left':
            start_x = self.x
            start_y = self.y - 1
            stop_x = self.x + 1
            stop_y = self.y + 1

        if self.cell_type == '-Right':
            start_x = self.x - 1
            start_y = self.y - 1
            stop_x = self.x
            stop_y = self.y + 1

        if self.cell_type == '-Top':
            start_x = self.x - 1
            start_y = self.y
            stop_x = self.x + 1
            stop_y = self.y + 1

        if self.cell_type == '-Bottom':
            start_x = self.x - 1
            start_y = self.y - 1
            stop_x = self.x + 1
            stop_y = self.y

        if self.cell_type == '-TopLeftRight':
            start_x = self.x
            start_y = self.y + 1
            stop_x = self.x
            stop_y = self.y + 1

        if self.cell_type == '-BottomLeftRight':
            start_x = self.x
            start_y = self.y - 1
            stop_x = self.x
            stop_y = self.y - 1

        if self.cell_type == '-LeftRight':
            start_x = self.x
            start_y = self.y - 1
            stop_x = self.x
            stop_y = self.y + 1

        if self.cell_type == '-TopBottomLeft':
            start_x = self.x + 1
            start_y = self.y
            stop_x = self.x + 1
            stop_y = self.y

        if self.cell_type == '-TopBottomRight':
            start_x = self.x - 1
            start_y = self.y
            stop_x = self.x - 1
            stop_y = self.y

        if self.cell_type == '-TopBottom':
            start_x = self.x - 1
            start_y = self.y
            stop_x = self.x + 1
            stop_y = self.y

        for y_iter in range(start_y, stop_y + 1):
            for x_iter in range(start_x, stop_x + 1):

                if (y_iter == self.y) and (x_iter == self.x):
                    continue

                if field[y_iter][x_iter] == '*':
                    counter += 1

        return counter


field_size = input()
lines, columns = field_size.split()
field = []

for i in range(int(lines)):
    line = input()
    field.append([ch for ch in line])

calc_field = []

for y in range(len(field)):
    y_list = []
    calc_field.append([])

    for x in range(len(field[y])):
        cell = Cell(x, y, field)

        if field[y][x] == '*':
            calc_field[y].append('*')
            print('*', end='')
        else:
            calc_field[y].append(cell.calculate_neighbours())
            print(cell.calculate_neighbours(), end='')

    print()
