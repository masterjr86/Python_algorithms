"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.

https://drive.google.com/file/d/1rzH4XYwKEkWZGgFJ_DdM2PSFMfl3q8Eh/view?usp=sharing
"""


# Допущение пользователь вводит целое неотрицательное число!

def invert(n):
    """ Функция принимает строку-число и возвращает целое число с обратным порядком цифр
    :param n: строка, состоящая из цифр
    :return: m, int
    """

    m = 0
    for i in reversed(range(len(n))):
        m += 10 ** i * (int(n) % 10)
        n = int(n) // 10
    return m


def invert_1(n):
    m = 0
    if len(n) == 1:
        m += int(n) // (len(n))
        return m
    else:
       m = (int(n) % 10)* 10 ** (len(n) -1) + invert(str(int(n) // 10))
       return m


n = input(f'Введите целое неотрицательное число: ')
m = invert(n)
m = invert_1(n)
print(f'Введённое число с цифрами в обратном порядке: {m}')
print(f'Введённое число с цифрами в обратном порядке (рекурсия): {m}')




