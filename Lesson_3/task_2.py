"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random as rnd

SIZE = 10

N_MIN = 0
N_MAX = 100

# Генерация массива, заполненного случайными числами.
array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]
# поиск четных элементов в первом массиве и сохранение их индексов во второй массив
array_2 = [id for id, itm in enumerate(array_1) if not itm % 2]

print(f'Исходный список: {array_1}')
print(f'Индексы исходного массива, в элементах котороых размещены четные числа: {array_2}')