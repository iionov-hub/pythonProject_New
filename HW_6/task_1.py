"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
ОС 64 версия питона 3.8"""
from pympler import asizeof
from numpy import array

my_list = ['зима', 'весна', 'лето', 'осень']
my_array = array(['зима', 'весна', 'лето', 'осень'])
print(asizeof.asizeof(my_list))
print(asizeof.asizeof(my_array))
v_month = int(input("Введите месяц в виде целого числа от 1 до 12 "))
if v_month == 12 or v_month == 1 or v_month == 2:
    print(my_list[0])
    print(my_array[0])
elif v_month == 3 or v_month == 4 or v_month == 5:
    print(my_list[1])
    print(my_array[1])
elif v_month == 6 or v_month == 7 or v_month == 8:
    print(my_list[2])
    print(my_array[2])
else:
    print(my_list[3])
    print(my_array[3])


## Вывод когда используем numpy (array) нам гораздо меньше требуется памяти
#в данном случае list затрачивает 440 array = 192
print('!!!!!!!!!!!!!!!!Следующий пример!!!!!!!!!!!!!!!!!!!!!!!')

class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_c(self):
        return round(self.width / 6.5 + 0.5,2)

    def get_j(self):
        return round(self.height * 2 + 0.3,2)

    @property
    def get_full(self):
        return str(f'Площадь общая ткани '
                   f' {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3),2)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Coat_sl(Textil):
    __slots__ = ['width', 'height']
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_full)
print(jacket.get_full)
print(jacket.get_c())
print(jacket.get_j())

print(coat.__dict__)
print(asizeof.asizeof((coat)))

coat  = Coat_sl(1, 2)
print(coat.__slots__)
print(asizeof.asizeof(coat))
## Здесь также вижу что слоты потребляют меньше памяти
#Обычный клас затрачивает 424 слоты в свою очередь
