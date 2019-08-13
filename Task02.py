"""
Известно, что любую обыкновенную дробь можно записать в виде конечной простой непрерывной дроби.
Напишите программу, которая преобразует обыкновенную дробь в последовательность коэффициентов a0,a1,…,an
"""

#num = "239/30"
num = input()

numerator = int(num.split("/")[0])
denominator = int(num.split("/")[1])

coefficients = list()
whole = 1
reminder = 1

while reminder != 0:
    whole = numerator // denominator
    reminder = numerator % denominator
    coefficients.append(whole)
    numerator = denominator
    denominator = reminder

for number in coefficients:
    print(number, end=" ")
