"""
Задача 35. Напишите функцию, которая принимает
одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5 Output: yes
"""
"""
def simple_number(n):
    if n > 10:
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            print(f'Введенное число {n} не является простым')
        elif n // n == 1 and n // 1 == n:
            print(f'Введенное число {n} является простым')
    else:
        if n == 1 or n == 2 or n == 3 or n == 5 or n == 7:
            print(f'Число {n} является простым')
        else:
            print(f'Введенное число {n} не является простым')
n = simple_number(int(input('Введите число: \n')))
"""
"""
решение на лекции через рекурсию
def is_prime(n, i=2):
    if n == 2 or i > int(n ** 0.5):
        return True
    if n % i == 0:
        return False
    return is_prime(n, i+1)


n = int(input("Введите число: "))
if is_prime(n):
    print(n, "является простым числом")
else:
    print(n, "не является простым числом")
"""


# Владимир поделился
def checking_number(n):
    numbers = []
    [numbers.append(int(i)) for i in range(1, n // 2 + 1) if n % i == 0]
    # print(numbers)
    result = f' является.' if len(numbers) <= 1 else f' не является.'
    print(f'Введенное число {n} простым' + result)


def main():
    n = int(input('Введите любое число: '))
    print('Получено следующее значение: ', n)
    checking_number(n)


if __name__ == 'main':
    main()


"""
Ришат решил через рекурсию
def recursive_input2(size_n: int):
    x = input('please input: ')
    if size_n == 1:
        print(x, end=' ')
    else:
        recursive_input2(size_n - 1)
        print(x, end=' ')


n = int(input('Please input number: '))

recursive_input2(n)
"""