"""
Задача 2.
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

Ссылка на алгоритм:
https://drive.google.com/file/d/1kfmj55BP0r2TTdRCvURNO_teIC6VbR4K/view?usp=sharing

Допущение: Известно, что числа 5 и 6 представляются в двоичной системе 3 битами.
"""

x = 5
y = 6

div_x0 = x // 2
div_y0 = y // 2

x0 = x % 2
y0 = y % 2

if x0 == 1 and y0 == 1:
    xy_mult0 = 1
    xy_sum0 = 1
else:
    if x0 == 0 and y0 == 0:
        xy_mult0 = 0
        xy_sum0 = 0
    else:
        xy_mult0 = 0
        xy_sum0 = 1

div_x1 = div_x0 // 2
div_y1 = div_y0 // 2

x1 = div_x0 % 2
y1 = div_y0 % 2

if x1 == 1 and y1 == 1:
    xy_mult1 = 1
    xy_sum1 = 1
else:
    if x1 == 0 and y1 == 0:
        xy_mult1 = 0
        xy_sum1 = 0
    else:
        xy_mult1 = 0
        xy_sum1 = 1

div_x2 = div_x1 // 2
div_y2 = div_y1 // 2

x2 = div_x1 % 2
y2 = div_y1 % 2

if x2 == 1 and y2 == 1:
    xy_mult2 = 1
    xy_sum2 = 1
else:
    if x2 == 0 and y2 == 0:
        xy_mult2 = 0
        xy_sum2 = 0
    else:
        xy_mult2 = 0
        xy_sum2 = 1

x_and_y = 2 ** 2 * xy_mult2 + 2 * xy_mult1 + xy_mult0
x_or_y = 2 ** 2 * xy_sum2 + 2 * xy_sum1 + xy_sum0

print(f'Результатом побитового И чисел {x} и {y} является число {x_and_y} ({xy_mult2}{xy_mult1}{xy_mult0})')
print(f'Результатом побитового ИЛИ чисел {x} и {y} является число {x_or_y} ({xy_sum2}{xy_sum1}{xy_sum0})')
