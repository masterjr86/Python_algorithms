"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections

num_fabrique = int(input('Введите количесвто предприятий: '))

fabriques = []

for i in range(num_fabrique):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Квартальная прибыль (через пробел): ').split(' '))
    fabrique = {
        'title': title,
        'profit_q1': profit_q1,
        'profit_q2': profit_q2,
        'profit_q3': profit_q3,
        'profit_q4': profit_q4,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    fabriques.append(fabrique)

profit_col = collections.Counter()
for fabrique in fabriques:
    profit_comp = fabrique.copy()
    del profit_comp['title']
    profit_col += collections.Counter(profit_comp)

average_profit = profit_col['profit_year'] / len(fabriques)

print('Средняя годовая прибыль компаний: ', average_profit)
print('Прибыль выше среднего: ', [x['title'] for x in fabriques if x['profit_year'] >= average_profit])
print('Прибыль ниже среднего: ', [x['title'] for x in fabriques if x['profit_year'] < average_profit])
