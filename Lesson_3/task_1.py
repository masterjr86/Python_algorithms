"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

N_START = 2
N_FINISH = 99

START_RANGE = 2
FINISH_RANGE = 9

# вариант 1 - ПЕРЕБОР
answer = {i: 0 for i in range(START_RANGE, FINISH_RANGE + 1)}

print(f'В диапазоне от {N_START} до {N_FINISH}:')
for i in range(START_RANGE, FINISH_RANGE + 1):
    for j in range(i, N_FINISH + 1):
        if j >= i and not j % i:
            answer[i] += 1
    print(f'{answer[i]} чисел кратны {i}')

# вариант 2.
answer_1 = {i: 0 for i in range(START_RANGE, FINISH_RANGE + 1)}

print(f'Вариант 2. В диапазоне от {N_START} до {N_FINISH}:')
for i in range(START_RANGE, FINISH_RANGE + 1):
    answer_1[i] = N_FINISH // i
    print(f'{answer_1[i]} чисел кратны {i}')
