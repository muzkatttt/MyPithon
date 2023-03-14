"""
Задача 11. Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи
оно является, то есть выведите такое число
n, что φ(n)=A. Если А не является числом Фибоначчи,
выведите число -1.
Input: 5 Output: 6
"""

sum = [0, 1]
i = 0
j = 1
index = 2

num = int(input("Введите число\n "))

while j < num:
    next_el = i + j
    sum.append(next_el)
    i = j
    j = next_el
    index += 1
print(sum)

if j == num:
    print(index)
else:
    print(-1)

# решение задачи про числа Фиббоначчи без коллекций
number = int(input("Введите целое число >= 2:\t "))

fib1 = 0
fib2 = 1
fib_sum = 0
index = 2

while number >= fib_sum:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    index += 1

if fib1 == number:
    print(index - 1)
else:
    print(-1)