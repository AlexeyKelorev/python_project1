"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('text.txt', 'w') as txt_file:
    while txt_file:
        input_str = input('Введите текст: ')
        txt_file.write(input_str)
        txt_file.write("\n")
        if not input_str:
            break

with open('text.txt', 'r') as txt_file:
    content = txt_file.read()
    print(content)
