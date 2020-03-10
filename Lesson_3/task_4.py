"""
Определить, какое число в массиве встречается чаще всего.

Допущение: Будет выведен один наиболе часто повторяющийся элемент
"""

import random as rnd

SIZE = 100

N_MIN = 0
N_MAX = 5

array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]

elem, expectation = 0, 0  # будет хранить элемент и количесвто таких элементов в массиве

print(array_1)
for i in range(len(array_1)):
    counter = 0
    for j in range(i + 1, len(array_1)):
        if array_1[j] == array_1[i]:
            counter += 1
    if counter + 1 > expectation:
        elem, expectation = array_1[i], counter + 1
print(f'В массиве чаще всего встречается число {elem}, {expectation} раз')
