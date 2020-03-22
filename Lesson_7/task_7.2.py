"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random
import timeit

n_min = 0
n_max = 10


SIZE = 5
array_float = [float('{:.3f}'.format(random.uniform(n_min, n_max))) for i in range(SIZE)]


def merge(arr_1,arr_2):
    sorted_array = []
    while arr_1 and arr_2:
        if arr_1[0] < arr_2[0]:
            sorted_array.append(arr_1.pop(0))
        else:
            sorted_array.append(arr_2.pop(0))
    if arr_1:
        sorted_array.extend(arr_1)
    if arr_2:
        sorted_array.extend(arr_2)
    return sorted_array


def mergesort(arr):
    if len(arr) == 1:
        return arr
    middle = int(len(arr) / 2)
    divide_list = merge(mergesort(arr[:middle]), mergesort(arr[middle:]))
    return divide_list

print(array_float)
print(mergesort(array_float))


# print(timeit.timeit('mergesort(array_float)',number=1000, globals=globals()))
# print(timeit.timeit('sorted(array_float)',number=1000, globals=globals()))