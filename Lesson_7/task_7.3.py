"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
 сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import statistics
import random

n_min = 1
n_max = 10
size = int(input(f'Введите натуральное число: '))
arr_inp = [random.randint(n_min, n_max) for i in range(2 * size + 1)]

arr_test = [1, 5, 3, 7, 9, 4, 65, 38,  6, 8, 2, 12, 53, 76, 32, 90, 45, 11, 43, 21, 31] # тестовый массив без повторов

# функция работает только с нечетным массивом без повторений !!!
def median_1(arr):
    assert len(arr) > 0
    if len(set(arr)) == 1:
        return arr[1]
    if len(set(arr)) == len(arr):
        for i in range(len(arr)):
            min_count, max_count = 0, 0
            for j in range(len(arr)):
                if j != i:
                    if arr[j] > arr[i]:
                        max_count += 1
                    elif arr[j] < arr[i]:
                        min_count += 1
                    else:
                        continue
            if min_count == max_count:
                return arr[i]
print(f'Тестовый массив без повторов {arr_test}')
print(f'Медиана массива без повторов полученная median_1: {median_1(arr_test)}, '
      f'медиана, рассчитання встроенной функцией: {statistics.median(arr_test)}')


def median_2(arr):
    dict_arr = {i:arr.count(i) for i in arr}
    mo = sum(dict_arr.values()) / 2
    median_interval = 0
    for i in range(n_min, n_max + 1):
        if i in dict_arr.keys():
            median_interval += dict_arr[i]
            if median_interval >= mo:
                return i

print(f'Тестовый массив с повтороами {arr_inp}')
print(f'Медиана ряда, полученная с помощью встроенной функции: {statistics.median(arr_inp)}')
print(f'Медиана ряда, полученная с помощью функции median_2: {median_2(arr_inp)}')

