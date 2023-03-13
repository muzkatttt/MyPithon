
# вариант решения задачи через лямбда функции


def filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
        return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# этот блок равен следующей записи через лямбду
"""def is_even(number):
    return number % 2 == 0
print(filter(numbers, is_even))
"""
# для четных чисел
print(filter(numbers, lambda number: number % 2 == 0))

# для нечетных чисел
"""def is_not_even(number):
    return number % 2 != 0
print(filter(numbers, is_not_even))
"""
print(filter(numbers, lambda number: number % 2 != 0))


# для чисел больше 4-х
"""
def big_4(number):
    return number > 4
print(filter(numbers, big_4))
"""
print(filter(numbers, lambda number: number > 4))
