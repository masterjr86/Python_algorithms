"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
"""

import cProfile
import math
import timeit


def sieve(m):
    len_sieve = int(2 * m * math.log(m))  # размер массива в 2 раза больше чем примерное значение m-го простого числа
    primes = [i for i in range(len_sieve)]
    primes[1] = 0
    for i in range(2, len_sieve):
        if primes[i] != 0:
            m -= 1
            if m == 0:
                return primes[i]
            j = i ** 2
            while j < len_sieve:
                primes[j] = 0
                j += i
    return primes


def prime(n):
    assert n > 0  # номер числа должен быть натуральным числом
    itm = 2
    while True:
        primes = []  # список бует хранить простые числа
        for i in range(2, itm + 1):
            divisors = []  # список будет хранить делители (или первый делитель)
            for j in range(2, i):
                if i % j == 0:
                    divisors.append(j)
                    # continue
            if not divisors:
                primes.append(i)
                if len(primes) == n:
                    return primes[-1]
                    break
        itm += 1


print(timeit.timeit('prime(5)', number=1000, globals=globals()))  # 0.043660500000000005
print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.4033945
print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 6.1604243
print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 83.4546058

cProfile.run('prime(5)')  # 67    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(10)')  # 711    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(20)')  # 5964    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(40)')  # 46855    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}

print(timeit.timeit('sieve(5)', number=1000, globals=globals()))  # 0.0077964000000037
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.01771880000001147
print(timeit.timeit('sieve(20)', number=1000, globals=globals()))  # 0.042993499999994356
print(timeit.timeit('sieve(40)', number=1000, globals=globals()))  # 0.10572409999998911

cProfile.run('sieve(5)')  #  5 function calls in 0.000 seconds
cProfile.run('sieve(10)')  # 711    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('sieve(20)')  # 5964    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
cProfile.run('sieve(40)')  # 46855    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}

"""
Выводы:
В первом случае (перебор делителей) я думаю, что алгоритм с экспоненциальной сложностью.
Во втором случае: сложность LOG(N).
"""