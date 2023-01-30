"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def division(*arg):
    try:
        return arg[0] / arg[1]
    except ZeroDivisionError:
        return "Вы что? Вытаетесь делить на 0!"


try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print(division(number1, number2))
except ValueError:
    print("Нужно ввводить числа")
