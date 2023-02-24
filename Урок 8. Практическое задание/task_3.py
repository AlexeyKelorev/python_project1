"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyError(Exception):
    def __init__(self, message):
        self.message = message

def is_number(unit):
    try:
        float(unit)
        return True
    except ValueError:
        return False

def examination(self):
    if not is_number(self):
        raise MyError('Ошибка данных')


data = input("Введите данные: ")
try:
    examination(data)
except MyError as err:
    exit(err)
