"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

https://drive.google.com/file/d/1rzH4XYwKEkWZGgFJ_DdM2PSFMfl3q8Eh/view?usp=sharing
"""

n = input(f'Введите целое натуральное число: ')
even = 0
not_even = 0

for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        not_even += 1
print(f'В ведённом числе {n} {even} чётных цифр и {not_even} нечётных')
