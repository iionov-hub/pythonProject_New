"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit, default_timer, repeat

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse_2(number, revers_num=0):
    if number // 10 == 0:
        revers_num += number % 10
        return revers_num
    return f'{number % 10}{recursive_reverse_2(number // 10)}'


setup = 'from __main__ import recursive_reverse'
print(repeat('recursive_reverse(14454545)', setup, default_timer, 3, 100000))

setup = 'from __main__ import recursive_reverse_2'
print(repeat('recursive_reverse_2(14454545)', setup, default_timer, 3, 100000))

