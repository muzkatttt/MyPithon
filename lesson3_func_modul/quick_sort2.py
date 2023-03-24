# быстрая сортировка
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
# в список будем записывать значение i, проходясь по массиву по циклу, начиная с 1 индекса элемента, т.к.
# 1-й элемент уже определен array[0], для этого используем срез списка [1:]
# через условие if добавляем только те значения, которые меньше либо равны pivot
    less = [i for i in array[1:] if i <= pivot]
# в список greater запишем все i больше переменной pivot
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater) # будем сортировать списки less и greater
print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))