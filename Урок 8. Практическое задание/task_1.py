"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def to_int(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def to_valid(param1, param2, param3):
        if (param1 in range(1, 32)) and (param2 in range(1, 13) and param3 in range(1900, 2024)):
            return True
        else:
            return False

    def __str__(self):
        return f'Текущая дата {Data.to_int(self.day_month_year)}'


today = Data('23 - 02 - 2023')
print(today)

print(Data.to_valid(32, 33, 12222))
print(today.to_valid(31, 12, 1980))
print(Data.to_int('11 - 11 - 2022'))
print(today.to_int('11 - 11 - 2022'))
