"""
Задача 6.
ВПользователь вводит номер буквы в алфавите. Определить, какая это буква.

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing

Допущение: Пользователь вводит номер буквы английского алфавита и знает,что их там 26.
"""


n = int(input('Введите номер буквы: '))
index = 96 + n
user_letter = chr(index)
print(user_letter)