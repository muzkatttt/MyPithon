from .nurses import get_nurses  # импорт функции из другого модуля


def get_surgeons():
    get_nurses()  # вызов функции внутри другой функции
    print('хируги из пакета доктора ')


get_surgeons()
