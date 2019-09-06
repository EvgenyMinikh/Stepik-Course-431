"""
Напишите простой интерпретатор математического выражения.
На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a operator b,
где вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения,
вычитания, умножения и целочисленного деления.
"""

in_str = input()
args = in_str.split()
first_number = int(args[0])
operator = args[1].lower()
second_number = int(args[2])

if operator == "plus":
    print(first_number + second_number)
elif operator == "minus":
    print(first_number - second_number)
elif operator == "multiply":
    print(first_number * second_number)
elif operator == "divide":
    print(first_number // second_number)
