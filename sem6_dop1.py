"""
Доп задача к семинару
Дано натуральное число n>1. Выведите все простые
множители этого числа в порядке неубывания с учетом
кратности. Алгоритм должен иметь сложность O(logn).

"""

def prime_factors(n, divisor=2):
    if n == 1:
        return
    if n % divisor == 0:
        print(divisor, end=" ")
        prime_factors(n//divisor, divisor)
    else:
        prime_factors(n, divisor+1)

def wer(n):
    for i in range(2, n+1):
        if n%i == 0:
            if i == n:
                return [i]
            else:
                return [i] + wer(n//i)


print(wer(144))
prime_factors(144)
"""
Внутри функции проверить, делится ли n на divisor без остатка. 
Если да, то вывести divisor и вызвать рекурсивно prime_factors(n//divisor, divisor).
Если n не делится на divisor, то увеличить divisor на 1 и вызвать рекурсивно prime_factors(n, divisor).
"""