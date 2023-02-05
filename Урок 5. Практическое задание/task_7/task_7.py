"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
 данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
profit = {}
pr = {}
sum_prof = 0
average_profit = 0
i = 0
with open('firms.txt', 'r') as content:
    for line in content:
        firm_name, form, revenue, costs = line.split()
        profit[firm_name] = int(revenue) - int(costs)
        if profit.setdefault(firm_name) >= 0:
            sum_prof = sum_prof + profit.setdefault(firm_name)
            i += 1
    if i != 0:
        average_profit = sum_prof / i
        print(f'Average_profit - {average_profit:.2f}')
    else:
        print('No profit')
    pr = {'Average_profit': round(average_profit)}
    profit.update(pr)
    print(f'Profit- {profit}')

with open('result.json', 'w') as write_json:
    json.dump(profit, write_json)
    js_str = json.dumps(profit)
