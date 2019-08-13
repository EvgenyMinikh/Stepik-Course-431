"""
Напишите программу, которая принимает на вход список чисел и число, после чего выводит все позиции,
на которых это число встречается в переданном списке.
"""

# user_numbers = "5 8 2 7 8 8 2 4"
# number_to_find = "8"
user_numbers = input()
number_to_find = input()

nums = user_numbers.split(" ")
position = 0
isNone = True

for num in nums:
    if num == number_to_find:
        isNone = False
        print(position, end=" ")
    position += 1

if isNone:
    print("None")
