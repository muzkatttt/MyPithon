# быстрая сортировка Хоара
from random import random


nums = [4, 1, 6, 3, 2, 7, 8]
n = 1
while n < len(nums):
    for i in range(len(nums) - n):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    n += 1
print(nums)
# Эта часть кода делит массив на две части, в одной из которых
# находятся элементы меньше определённого значения,
# а в другой – больше или равные.

# def quicksort(nums):
#    if len(nums) <= 1:
#        return nums
#    else:
#       q = random.choice(nums)
#        s_nums = []
#        m_nums = []
#        e_nums = []
#        for n in nums:
#            if n < q:
#                s_nums.append(n)
#            elif n > q:
#                m_nums.append(n)
#            else:
#                e_nums.append(n)
#        return quicksort(s_nums) + e_nums + quicksort(m_nums)


# сортировкa Хоара в функциональном виде
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


# print(quicksort)
