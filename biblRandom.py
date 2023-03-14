# random позволяет генерировать случайные
# числа, буквы, эдементы последовательности

# основные функции
"""
randint - целое случайное число от А до В
choice - случайный элемент последовательности
shuffle - перемешивает последовательность
random - случайное число от 0 до 1
sample - список длиной k из последовательности
"""
from random import randint, choice, sample, shuffle
# 1. Загадать случайное число от 0 до 100
print(randint(1, 100))

# 2. выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))

print('\n')
# 3. выбрать 3-х победителей лотереи из списка players
print(sample(players, 3))
print('\n')
# 4. перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)
