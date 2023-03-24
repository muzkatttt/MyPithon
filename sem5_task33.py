"""
Задача N33. Хакер Василий получил доступ к классному журналу
и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот:
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
"""

def student_evaluations(n):
    min = 1
    max = 5
    if n == min:
        return max
    return student_evaluations(n-1) - min

print(student_evaluations(n = int(input('Введите оценку: \n'))))

