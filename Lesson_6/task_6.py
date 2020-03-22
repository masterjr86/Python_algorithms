"""
Алгоритм решения задачи:
1. Предыдущее решение загнали в функцию, которая возвращает словарь с переменныи.
2. Функция, написанная на уроке умеет "работать" со словарем, поэтому можно ей в качесвте агрумента передавать
   функцию из п.1

"""

import random as rnd
import sys


def min_elems(size, min_elem, max_elem):
    SIZE = size
    N_MIN = min_elem
    N_MAX = max_elem

    array_1 = [rnd.randint(N_MIN, N_MAX) for i in range(SIZE)]

    min_elem = [array_1[0], array_1[1]]
    for i in array_1[2:]:
        if i <= min_elem[0] and min_elem[0] <= min_elem[1]:
            min_elem[0], min_elem[1] = i, min_elem[0]
        elif i <= min_elem[0] and min_elem[0] > min_elem[1]:
            min_elem[0] = i
        elif i > min_elem[0] and i < min_elem[1]:
            min_elem[1] = i
    return locals() #(f'Два наименьших элемента в исходном массиве: {min_elem[0]}, {min_elem[1]}')


def var_size(obj):
    variable_size = sys.getsizeof(obj)
    # print(f'type = {type(obj)}, size = {sys.getsizeof(obj)}, obj= {obj}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                variable_size += sys.getsizeof(key)
                variable_size += sys.getsizeof(value)
        elif not isinstance(obj, str):
            for item in obj:
                var_size(item)
                variable_size += sys.getsizeof(item)
    return f'Размер памяти: {variable_size} байт'


# Python 3.8.1, 64, OC - 64
print(var_size(min_elems(100, -2233, 32423)))
print(var_size(1))
print(var_size('python'))
print('Python 3.8.1, 64, Win - 64')

