"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random as rnd
import functools as fct

SIZE = 10000

N_MIN = -1000
N_MAX = 1000

array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]

elem_min, min_id = array_1[0], 0
elem_max, max_id = array_1[1], 0

for id, itm in enumerate(array_1):
    if itm > elem_max:
        elem_max = itm
        max_id = id
    if itm < elem_min:
        elem_min = itm
        min_id = id

print(array_1, (elem_min, min_id), (elem_max, max_id))
print(fct.reduce(lambda x, y: x + y, array_1[min_id + 1:max_id]) if min_id < max_id \
          else fct.reduce(lambda x, y: x + y, array_1[max_id + 1:min_id]))

# print(sum(array_1[min_id + 1:max_id]) if min_id < max_id else sum(array_1[max_id + 1:min_id]))
