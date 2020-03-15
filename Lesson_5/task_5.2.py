"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

hex_dict = {  # словарь шесстнадцатиричных символов
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}

hex_list = list(hex_dict.keys())  # сключи словаря для удобства


def sum_hexadicimal(hexnum_1, hexnum_2):
    """
    :param hexnum_1:  первое шестнадцатиричное число
    :param hexnum_2:  второе шестнадцатиричное число
    :return:
    """
    c = collections.deque([0 * (len(max(hexnum_1, hexnum_2)) + 1)])  # результат сложения
    a, b = collections.deque(hexnum_1.lower()), collections.deque(hexnum_2.lower())  # преобразоватние строки в список
    min(a, b).extendleft([0 for i in range(len(max(a, b)) - len(min(a, b)))])  # контроль размерности списков

    over = 0  # индекс переполнения разряда
    for i in reversed(range(len(a))):
        j = hex_dict[str(a[i])] + hex_dict[str(b[i])]
        if j + over <= 15:
            c.appendleft(hex_list[(hex_dict[str(a[i])] + hex_dict[str(b[i])]) % 16 + over])
            over = 0
        else:
            c.appendleft(hex_list[(hex_dict[str(a[i])] + hex_dict[str(b[i])]) % 16 + over])
            over = 1
    return [i for i in list(c) if i != 0]


print(sum_hexadicimal('A2', 'c4f'))
print(sum_hexadicimal('39bd', 'fa12c'))

# блок проверки
assert (sum_hexadicimal('2f', '2f') == ['5', 'e'])
assert (sum_hexadicimal('39bd', 'fa12c') == ['f', 'd', 'a', 'e', '9'])
