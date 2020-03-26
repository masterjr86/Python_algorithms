"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit

SIZE = 200

array_int = [random.randint(-100, 99) for i in range(SIZE)]

# функция сортировки массива исходная (из ввидеоурока)
def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr

# функция сортировки массива усовершенствованная
def bubble_sort_mod(arr):
    for i in range(1, len(arr)):
        for k in range(0, len(arr) - i):
            if arr[k] < arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr

print(f'Исходный массив{array_int}')
print(f'Массив отсортированный исходной функцией:{bubble_sort(array_int)}')
print(f'Массив отсортированный усовершенствованной функцией:{bubble_sort_mod(array_int)}')

# этот блок - проверка времени сортировки
time_buble = timeit.timeit('bubble_sort(array_int)', number=1000, globals=globals())
time_buble_mod = timeit.timeit('bubble_sort_mod(array_int)', number=1000, globals=globals())
print(f'Время сортировки 1 функции: {time_buble}')
print(f'Время сортировки 1 функции: {time_buble_mod}') # алгоритм работает немного быстрее
