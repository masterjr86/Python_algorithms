"""
Задача 1.
Найдите сумму цифр трёхзначного числа

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing
"""

# алгоритм не исколючает 0 при умножении
X = int(input('Введите трёхзначное число: '))
hund = X // 100
tens = (X // 10) % 10
ones = X % 10
sum_X = hund + tens + ones
mult_X = hund * tens * ones
print(f'Сумма цифр числа {X} равна {sum_X}, произведение цифр равно {mult_X}')

# код ниже для проверки
# for i in range(100, 1000, 1):
#     print(i, i // 100, (i // 10) % 10, i % 10)
#     print(i // 100 + (i // 10) % 10 + i % 10)
#     print((i // 100) * ((i // 10) % 10) * (i % 10))
