"""
Задача 8.
Определить, является ли год, который ввел пользователь, високосным или не високосным.

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing

Предполагается, что пользователь знает про Григорианский календарь и вводит целое натуральное число.
"""

year = int(input("Введите год: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} год високосный')
        else:
            print(f'{year} год не високосный')
    else:
        print(f'{year} год високосный')
else:
    print(f'{year} год не високосный')
