# Пузырьковая сортировка от меньшего к большему

from task_random import randint

N = 30
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print(a)  # вывод на печать
