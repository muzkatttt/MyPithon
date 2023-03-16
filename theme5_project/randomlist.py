"""
создать модуль. В нем создать функцию,
которая принимает список и возвращает из
него случайный элемент. Если список пустой,
то функция должна вернуть None. Проверьте
работу функций в этом же модуле
"""
import random
def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result # else можно не указывать, т.к.
        # Пайтон возвращает None, если значение не будет найдено

"""
тоже самое нужно сделать в модулях folders.py и
randomlist.py и сдвинуть вызов функций под конструкцию
if __name__ == 'main':
"""
if __name__ == 'main':
    print(get_random([1, 2, 3, 4]))
    print(get_random([]))