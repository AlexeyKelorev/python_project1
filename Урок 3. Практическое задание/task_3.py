"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))


def my_func2(*args):
    print(sum(list(args)) - min(list(args)))


if __name__ == '__main__':
    my_func1(322, 150, 200)
    my_func2(322, 150, 200)
