def sum_numbers(n):
    summ = 0
    for i in range(1, n + 1):
        summ += 1
    print(summ)
sum_numbers(5)

#2 вариант записи кода
def sum_numbers(n):
    summ = 0
    for i in range(1, n + 1):
        summ += 1
    return summ # после return функция ничего не считает
print(sum_numbers(5))

# в переменную можно присвоить функцию
# a = sum_numbers(5)
#
