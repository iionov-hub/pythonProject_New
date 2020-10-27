"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from pympler import asizeof
import timeit

newlist = []
oldlist = ['test']

def doit1():
    for word in oldlist:
        newlist.append(word.upper())
    ## print(newlist)

def doit2():
    newlist = map(str.upper, oldlist)

doit1()
doit2()


t = timeit.Timer(setup='from __main__ import doit1', stmt='doit1()')
print(t.timeit())

t = timeit.Timer(setup='from __main__ import doit2', stmt='doit2()')
print(t.timeit())
"""Вместо цикла можно использовать функцию map, map также может конвертацию из текста в числа что очень удобно"""