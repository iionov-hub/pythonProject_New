"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def task6(count, n_num):

    print(f"Попытка №{count}")
    answer = int(input("Введите число от 0 до 100: "))



    if count == 10 or answer == n_num:
        if answer == n_num:
            print("Верно!")
        print(f"Загаданное число: {n_num}")
    else:
        if answer > n_num:
            print(f"Загаданное число меньше чем {answer}")
        else:
            print(f"Загаданное число больше чем {answer}")
        task6(count + 1, n_num)


n_num = random.randint(0, 100)
task6(1, n_num)
