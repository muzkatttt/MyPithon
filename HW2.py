"""
Задача 2. Найдите сумму цифр
трехзначного числа
"""
number = int(input('Введите число: '))

sum = 0
temp = 0
while number > 0:
    temp = number % 10
    sum += temp
    number = number // 10

print(sum)
