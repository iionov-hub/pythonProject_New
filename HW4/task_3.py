"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit, default_timer, repeat

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


statement = [
    ['revers(782734826364)', 'revers'],
    ['revers_2(782734826364)', 'revers_2'],
    ['revers_3(782734826364)', 'revers_3']
]

for st in statement:
    print(repeat(st[0], f'from __main__ import {st[1]}', default_timer, 3, 100000))

"""Самая быстрая функция 3, т.к. там нет вычислений"""