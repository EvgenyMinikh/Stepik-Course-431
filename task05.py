"""
Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения,
которые повторяются в нём более одного раза.
"""

input_numbers = input()
numbers = input_numbers.split(" ")

unique_nums = set(numbers)

for num in unique_nums:
    numbers.remove(num)

non_unique_nums = sorted(list(set(numbers)))

for num in non_unique_nums:
    print(num, end=" ")