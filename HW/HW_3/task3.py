"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

def func(s):
    h_str = hashlib.sha1(s.encode('utf-8')).hexdigest()
    sum_ = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            hash_subs = hashlib.sha1(s[i : j].encode('utf-8')).hexdigest()
            print(s[i: j])
            print(hash_subs)
            if  hash_subs != h_str:
                sum_.add(hash_subs)

    return len(sum_)


print(func('papa'))