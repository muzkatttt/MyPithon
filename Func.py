# abs, min, max, round, sum, enumerate

# модуль числа
print(abs(-7))
print('\v')  # вертикальная табуляция

# min, max
numbers = [1, 4, -4, 9, 0]
print(min(numbers))
print(max(numbers))
print('\n')  # перевод строки

# round в скобках указывать 2 аргумента: число и
# количество знаков после запятой для округления
print(round(10.9864814, 2))

# sum
print(sum(numbers))

# enumerate
winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)
