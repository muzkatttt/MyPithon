"""
Задача 36: Напишите функцию print_operation_table(operation,
num_rows=6, num_columns=6), которая принимает в качестве аргумента
функцию, вычисляющую элемент по номеру строки и столбца. Аргументы
num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет
с единицы (подумайте, почему не с нуля). Примечание: бинарной
операцией называется любая операция, у которой ровно два аргумента,
как, например, у операции умножения.
*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

"""
def print_operation_table(operation, rows, columns):
    rows = 6
    columns = 6
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(i * j, end=' \t') #end=' '*4 - ставится 4 пробела после произведения чисел
        print('\n')

print_operation_table(lambda x, y: x * y, 6, 6)