# пользователь вводит 3 числа
# Найти минимальное и максимальное значение и их сумму,
# результат вывести на экран

numbers = []

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
