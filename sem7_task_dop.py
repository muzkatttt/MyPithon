from datetime import datetime
from time import sleep


def time_now(msg, *, dt=datetime.now()):
    print(msg, dt)


# Тесты
time_now('Сейчас такое время: ')
sleep(1)
time_now('Прошла секунда: ')
sleep(1)
time_now('Ничего не понимаю... ')

import time

def main(func):

    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print('Время работы:', time.time() - start)
        return result

    return wrapper

@main
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == '__main__':
    print(get_nod(1000, 50))