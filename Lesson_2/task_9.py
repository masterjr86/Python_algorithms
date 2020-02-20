"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

https://drive.google.com/file/d/1rzH4XYwKEkWZGgFJ_DdM2PSFMfl3q8Eh/view?usp=sharing
"""


def sum_digit(n):
    """
    Функция возвращает сумму цифр числа
    :param n: Строка, состоящая из цифр
    :return: Сумма цифр
    """
    sum_digit = 0
    for i in n:
        sum_digit += int(i)
    return sum_digit


n = input(f'Введите числа через пробел: ').split()
sum_digit_max = 0
m = 0

for i in n:
    if int(sum_digit(i)) > sum_digit_max:
        sum_digit_max = sum_digit(i)
        m = i
print(f'Среди введённых чисел наибольшая сумма цифр у числа {m}, {sum_digit_max}')
