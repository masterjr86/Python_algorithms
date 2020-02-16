"""
Задача 5.
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing

Допущение: Пользователь вводит номер буквы английского алфавита.
"""

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

index_a = ord(a) - 96
index_b = ord(b) - 96
diff_ab = abs(index_a - index_b) - 1
print(f'Буква {a} находится на {index_a} месте в алфавите')
print(f'Буква {b} находится на {index_b} месте в алфавите')
print(f'Между {a} и {b} находится {diff_ab} букв')