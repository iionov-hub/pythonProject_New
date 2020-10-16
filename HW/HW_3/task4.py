"""
Задача 4.
Реализуйте скрипт "Кеширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
my_dict = {}

def task4(url):
    if my_dict.get(url):
        print(f'Есть страница : {url}  в кэше')
    else:
        my_dict[url]  = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ":" + salt
        print(my_dict)
task4('https://geekbrains.ru/')
task4('https://mail.ru/')
task4('https://geekbrains.ru/')
task4('https://mail.ru/')