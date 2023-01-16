"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = input("Введите целое положительное число n: ")
result = int(number) + int(number+number) + int(number+number+number)
print(f"{number} + {number+number} + {number+number+number} = {result}")
