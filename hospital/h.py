from .doctors.surgeons import get_surgeons
""" импорт функции get_surgeons
пакета .doctors из модуля surgeons в папке doctors
"""


def get_main():
    print('Мед')
    get_surgeons()


get_main()
