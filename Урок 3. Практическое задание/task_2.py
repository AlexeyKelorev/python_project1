"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_user_data(**kwargs):

    print(f'Имя: {kwargs.get("name")}, фамилия: {kwargs.get("surname")},'
          f' год рождения: {kwargs.get("birth_year")}, город проживания: {kwargs.get("city")},'
          f' email: {kwargs.get("email")}, телефон: {kwargs.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Иван',
        'surname': 'Иванов',
        'birth_year': '1846',
        'city': 'Москва',
        'email': 'jackie@gmail.com',
        'phone': '01005321456',
    }
    print_user_data(**user)
