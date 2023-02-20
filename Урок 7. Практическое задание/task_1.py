"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

class Matrix:
    def __init__(self, *args):
        self.cl_matr = list(args)
        self.out_mat = list(args)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.cl_matr])

    def __add__(self, other):
        out_line_matr = []
        out_matr = []
        for i in range(len(self.cl_matr)):
            for j in range(len(self.cl_matr[i])):
                out_line_matr.append(self.cl_matr[i][j] + other.cl_matr[i][j])
            out_matr.append(out_line_matr)
            out_line_matr = []
        return out_matr


mat1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
mat2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(type(mat1))
print(mat2)


print(f"{mat1 + mat2}")
mat3 = mat1+mat2
result = Matrix(mat3)
print(type(result))

print(result)









