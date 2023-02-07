"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('numbers.txt', 'w') as in_content:
    input_numbers = input('Введите числа через пробел: ')
    in_content.writelines(input_numbers)

with open('numbers.txt', 'r') as out_content:
    numbers = out_content.readline()
    print(sum(map(int, numbers.split())))
