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

"""
# решение задачи у Владимира

def get_value_fib(fib, n):
    fib.append(fib[-2] + fib[-1])
    if len(fib) == n:
        return fib
    return get_value_fib(fib, n)


def main():
    fib = [0, 1]
    n = int(input('Введите длину последовательности: '))
    print(get_value_fib(fib, n))


if name == 'main':
    main()


# у Ришата
num = int(input('Please input number: '))


def fibonachy(n: int):
    if n == 0 or n == 1:
        return n
    return fibonachy(n - 1) + fibonachy(n - 2)


print(fibonachy(num))
"""