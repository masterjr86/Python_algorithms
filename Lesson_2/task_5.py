"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

https://drive.google.com/file/d/1rzH4XYwKEkWZGgFJ_DdM2PSFMfl3q8Eh/view?usp=sharing
"""

n = 32
m = 127
for i in range(n, m + 1):
    print(i, chr(i), end=',')
    if (i - 1) % 10 == 0:
        print(';')
