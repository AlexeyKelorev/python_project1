"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

output_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i-1]]
print(output_list)

output_gen = (input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i-1])

result = list(output_gen)
print(result)
