"""
На вход программе подаётся строка, содержащая слова, разделённые пробелом.
Программа должна вывести статистику длин слов в полученной строке, от меньшей длины слова к большей (см. пример).
Словом считается последовательность произвольных символов, окружённая пробелами либо границами строки.
Заметьте, что знаки препинания также относятся к слову.
"""

input_string = input()

word_list = input_string.split(" ")
map_of_words = dict()

for word in word_list:
    if map_of_words.get(len(word)) is None:
        map_of_words[len(word)] = 1
    else:
        map_of_words[len(word)] = map_of_words[len(word)] + 1

key_list = map_of_words.keys()
key_list = sorted(key_list)

for key in key_list:
    print("{k}: {v}".format(k=key, v=map_of_words[key]))