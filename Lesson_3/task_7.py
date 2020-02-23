"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random as rnd

SIZE = 20

N_MIN = -20
N_MAX = 30

array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]

min_elem = [array_1[0], array_1[1]]
for i in array_1[2:]:
    if i <= min_elem[0] and min_elem[0] <= min_elem[1]:
        min_elem[0], min_elem[1] = i, min_elem[0]
    elif i <= min_elem[0] and min_elem[0] > min_elem[1]:
        min_elem[0] = i
    elif i > min_elem[0] and i < min_elem[1]:
        min_elem[1] = i

print(array_1)
print(f'Два наименьших элемента в исходном массиве: {min_elem[0]}, {min_elem[1]}')
