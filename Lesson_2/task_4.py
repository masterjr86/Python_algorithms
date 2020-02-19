"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

https://drive.google.com/file/d/1rzH4XYwKEkWZGgFJ_DdM2PSFMfl3q8Eh/view?usp=sharing
"""


def sum_series(n):
    """
    Функция рассчитывает сумму ряда, где первый член равен 1, в каждяй следующий меньше предыдущего в 2 раза по модулю
    и с противоположным знаком.
    :param n: количество элементов ряда, str
    :return: Сумма ряда
    """

    elem = 1
    sum_ser = 1
    k = -1
    while n != 1:
        elem = elem / 2
        sum_ser += k * elem
        k *= -1
        n -= 1
    return sum_ser


n = int(input(f'Введите количесвто элементов ряда: '))
summa = sum_series(n)
print(f'Сумма ряда равна: {summa}')
