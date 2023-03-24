"""
Задача No31. Последовательностью Фибоначчи
называется последовательность чисел a0, a1,
..., an, ..., где a0 = 0, a1 = 1, ak = ak-1
+ ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7 Output: 21
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Введите номер числа в последовательности: \n'))
list_fib = []
for i in range(1, n + 1):
    list_fib.append(fibonacci(i))
print(list_fib)
print('\t')
print(f'Число в последовательности: {fibonacci(i)}')

