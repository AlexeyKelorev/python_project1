"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

change_table = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open('file.txt', 'r') as content:
    for item in content:
        print(item)
        print(type(item))
        item = item.split(' ', 1)
        print(type(item))
        rus_file.append(change_table[item[0]] + ' ' + item[1])
        print(rus_file)
    print(rus_file)

with open('rus_file.txt', 'w') as rus_content:
    rus_content.writelines(rus_file)
