"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random as rnd

SIZE = 100

N_MIN = 0
N_MAX = 200

array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]

max_elem, max_id = array_1[0], 0
min_elem, min_id = array_1[1], 0

print(f'Иcходный массив: {array_1}')

for id, itm in enumerate(array_1):
    if itm > max_elem:
        max_elem = itm
        max_id = id
    if itm < min_elem:
        min_elem = itm
        min_id = id
print(f'Минимальный элемент = {min_elem} и находится в позиции {min_id}')
print(f'Максимальный элемент = {max_elem} и находится в позиции {max_id}')

array_1[min_id], array_1[max_id] = max_elem, min_elem
print(f'Изменённый массив: {array_1}')
print(f'Минимальный элемент  = {min_elem} и находится в позиции {max_id}')
print(f'Максимальный элемент  = {max_elem} и находится в позиции {min_id}')
