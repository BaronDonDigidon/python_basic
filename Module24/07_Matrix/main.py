from typing import List


class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        """Создаёт пустую матрицу заданного размера (заполненную нулями)."""
        self.rows: int = rows
        self.cols: int = cols
        self.data: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self) -> str:
        """Возвращает строковое представление матрицы."""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def add(self, other: 'Matrix') -> 'Matrix':
        """Складывает текущую матрицу с другой и возвращает результат."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера для сложения.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other: 'Matrix') -> 'Matrix':
        """Вычитает другую матрицу из текущей и возвращает результат."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера для вычитания.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other: 'Matrix') -> 'Matrix':
        """Перемножает текущую матрицу с другой и возвращает результат."""
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self) -> 'Matrix':
        """Возвращает транспонированную матрицу (поворот строк и столбцов)."""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result



# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())