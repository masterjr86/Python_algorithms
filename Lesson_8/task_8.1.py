"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
"""

import hashlib

def substring_find(string):
    assert len(string) > 0
    hash_list = set()
    iter = 1
    while iter < len(string):
        for i in range(len(string)):
            hash_tmp = hashlib.sha1(string[i:i + iter].encode('utf-8')).hexdigest()
            hash_list.add(hash_tmp)
        iter += 1
    return f'В указанной строке {len(set(hash_list))} различных подстрок'


print(substring_find('a a '))
