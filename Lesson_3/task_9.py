"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random as rnd

RAWS = 10
COLUMN = 5

N_MIN = -100
N_MAX = 100

# генерация матрицы 5х4, заполненной случайными числами
matrix = [[rnd.randint(N_MIN, N_MAX) for _ in range(COLUMN)] for _ in range(RAWS)]
min_elements = [N_MAX] * len(matrix[0])


# print(*matrix, sep='\n')
# поиск минимальных значений в каждом столбце
for i in range(RAWS):
    for j in range(COLUMN):
        print(f'{matrix[i][j]:>4}', end='|')
        if matrix[i][j] < min_elements[j]:
            min_elements[j] = matrix[i][j]
    print()

# поиск максимального значения среди найденных минимальных значений
max_elem = min_elements[0]
for itm in min_elements[1:]:
    if itm > max_elem:
        max_elem = itm

print(f'Минимальные значения в столбцах {min_elements}')
print(f'Максимальный элемент среди найденных минимальных: {max_elem}')