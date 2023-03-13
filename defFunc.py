# функция простой разделитель

def print_sep():
    # знак * означает дублирование заданной последовательности в строках
    print('-' * 100)


print('Моя первая функция')
print_sep()
print('Красивый разделитель')
print_sep()
print('Что, если функций будет много?')
print_sep()
print_sep()
print_sep()
print_sep()

print('\v')  # перевод строки

# функция простой разделитель


def get_sep(sep, sep_len):
    return sep * sep_len


# меняем знак разделителя
print(get_sep('*', 100))
print(get_sep('-', 100))

# меняем знак и длину разделителя
print(get_sep('*', 50))

# используем разделитель в тексте
sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)

print(text)
