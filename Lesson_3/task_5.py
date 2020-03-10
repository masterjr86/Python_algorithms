"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random as rnd

SIZE = 20000

N_MIN = -10000
N_MAX = 10000

array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]
max_negative, negative_ind = N_MIN, 0

for id, itm in enumerate(array_1):
    if not itm + abs(itm):
        if itm and (abs(itm) < abs(max_negative)):
            max_negative, negative_ind = itm, id

print(f'Исходный массив: {array_1}')
print(f'Максимальное отрицательное число: {max_negative} в позиции {negative_ind}')
