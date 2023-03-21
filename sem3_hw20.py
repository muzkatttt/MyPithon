"""
Задача 20
Напишите функцию, которая принимает словарь с параметрами
и возвращает строку запроса, сформированную из отсортированных
в лексикографическом порядке параметров.
Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))
должен возвращать строку:
challenge=17&course=python&lesson=2

"""
dictionary = {
    'course':'python',
    'lesson':2,
    'challenge':17}
sorted(dictionary)
print('&'.join(sorted(f'{k}={v}' for k, v in dictionary.items())))

