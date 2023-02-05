"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
sum_salary = 0
small_salary = []
with open('statement.txt', 'r') as statement:
    family_salary = statement.readlines()
    total_employees = len(family_salary)

    for item in family_salary:
        item = item.split()
        sum_salary += float(item[1])
        if float(item[1]) < 20000:
            small_salary.append(item[0])

    print("Меньше 20000 рублей получают:")
    print('\n'.join(small_salary))
    average_salary = round(sum_salary / total_employees, 2)
    print(f"Cредний оклад: {average_salary}")

