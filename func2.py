def filter(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
        return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(filter(numbers))


# второй вариант решения задачи (функциональный)


def filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
        return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print('\n')
# функция нахождения четных чисел в массиве


def is_even(number):
    return number % 2 == 0


print(filter(numbers, is_even))
print('\n')
# функция нахождения нечетных чисел в массиве


def is_not_even(number):
    return number % 2 != 0


print(filter(numbers, is_not_even))

# функция нахождения чисел больше 4-х

print('\n')


def big_4(number):
    return number > 4


print(filter(numbers, big_4))
