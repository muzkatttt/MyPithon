""""
Чтобы лучше разобраться в типах параметров функций Инна создала
inspect_function(), которая в качестве аргумента принимает
другую функцию (главное, не встроенную, built-in).
В результате работы она выводит следующие данные:
название анализируемой функции, наименование всех принимаемых
ею параметров и их типы (позиционные, ключевые и т.п.).
Попробуйте повторить результат девушки.
def my_func(a, b, c, d, *args):
pass
import inspect

Анализируем функцию my_func
a: POSITIONAL_ONLY
b: POSITIONAL_ONLY
c: POSITIONAL_OR_KEYWORD
d: POSITIONAL_OR_KEYWORD
args: VAR_POSITIONAL
e: KEYWORD_ONLY
f: KEYWORD_ONLY
kwargs: VAR_KEYWORD
"""
