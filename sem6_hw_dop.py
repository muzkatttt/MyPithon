
import itertools

s = '1111100000000'
com_set = itertools.combinations(s, 13)
for i in com_set:
    print(i)
