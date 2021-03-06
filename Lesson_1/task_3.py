"""
Задача 3.
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing
"""

print("Введите координаты 2 точек")
x1 = float(input('Введите координату x точки 1: '))
y1 = float(input('Введите координату y точки 1: '))
x2 = float(input('Введите координату x точки 1: '))
y2 = float(input('Введите координату x точки 1: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Уравнение прямой, проходящей через точки с координатами ({x1},{y1}) и ({x2}, {y2}): y = {k:.2f}x + {b:.2f}')
