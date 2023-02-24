"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class Stock:

    def __init__(self, type_mashine, model, quantity):
        self.type_mashine = type_mashine
        self.model = model
        self.quantity = quantity
        self.my_units = {'Единица товара: ': self.type_mashine, 'Модель': self.model, 'Количество': self.quantity}

    def admission(self, type_mashine, model, quantity):
        self.type_mashine = type_mashine
        self.model = model
        self.quantity = int(quantity)
        



class Mashines:
    def __init__(self, model, serial):
        self.model = model
        self.serial = serial

class Printer:
    def __init__(self, model, serial, speed):
        self.model = model
        self.serial = serial
        self.speed = speed

class Scaner:
    def __init__(self, model, serial, resolution):
        self.model = model
        self.serial = serial
        self.resolution = resolution

class Copyer:
    def __init__(self, model, serial, paper_size):
        self.model = model
        self.serial = serial
        self.paper_size = paper_size




