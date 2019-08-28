"""
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.
"""


class Card:
    cards_values = {"1": 10, "6": 6, "7": 7, "8": 8, "9": 9, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, card, main_suite):
        self.suite = card[-1]       # Масть
        self.value = card[0]        # Значение
        self.is_main_suite = False  # Козырная карта?

        if self.suite == main_suite:
            self.is_main_suite = True

    def __repr__(self):
        return "Card: " + self.value + self.suite

    def __eq__(self, o: object):
        if (self.suite == o.suite) and (self.value == o.value):
            return True
        return False

    def __lt__(self, o: object):
        if self.is_main_suite and (not o.is_main_suite):
            return False

        if (not self.is_main_suite) and (o.is_main_suite):
            return True

        if self.suite == o.suite:
            return Card.cards_values[self.value] < Card.cards_values[o.value]

        return None

    def __gt__(self, o: object):
        if self.is_main_suite and (not o.is_main_suite):
            return True

        if (not self.is_main_suite) and (o.is_main_suite):
            return False

        if self.suite == o.suite:
            return Card.cards_values[self.value] > Card.cards_values[o.value]

        return None


# input_str = "10S 6S"
# input_main = "S"

input_str = input()
input_main = input()

cards = input_str.split()

first_card = Card(cards[0], input_main)
second_card = Card(cards[1], input_main)

if first_card > second_card:
    print("First")
elif first_card < second_card:
    print("Second")
else:
    print("Error")
