"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                for j in range(6):
                    print(6-j, end='')
                    sleep(1)
                    print('\r', end='')
            elif i == 1:
                for j in range(2):
                    print(2 - j, end='')
                    sleep(1)
                    print('\r', end='')
            elif i == 2:
                for j in range(6):
                    print(6-j, end='')
                    sleep(1)
                    print('\r', end='')
            print("\r", end="")
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
