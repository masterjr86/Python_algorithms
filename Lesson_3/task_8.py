"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
raws = 4
column = 5


matrix_test = [[0 for i in range(raws)] for j in range(column)]

for i in range(column):
    sum_elem = 0
    for j in range(raws):
        if j < raws - 1:
            matrix_test[i][j] = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
            sum_elem += matrix_test[i][j]
        else:
            matrix_test[i][j] = sum_elem
        print(end='')
    print()

print(*matrix_test, sep='\n')
