"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} стоит'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} - {self.speed}. Превышение'
        else:
            return f'Скорость {self.name} - {self.speed}.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} - {self.speed}. Превышение!!!'
        else:
            return f'Скорость {self.name} - {self.speed}.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} машина полиции'
        else:
            return f'{self.name} гражданский автомобиль'


porshe = SportCar(100, 'черный', 'Porshe', False)
solaris = TownCar(30, 'серебристый', 'Solaris', False)
largus = WorkCar(70, '<белый>', 'Largus', False)
ford = PoliceCar(110, 'белый', 'Ford', True)

print(porshe.turn_left())
print(f'{largus.turn_right()}, {solaris.stop()}')
print(f'{ford.go()}. {ford.show_speed()}')
print(f'{porshe.name} {porshe.color}')
print(solaris.show_speed())
print(largus.show_speed())
print(ford.police())
print(ford.show_speed())
