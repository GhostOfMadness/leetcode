"""
Set Matrix Zeroes.

Необходимо выполнить следующее преобразование: если элемент матрицы равен 0,
то все значения в его строке и столбце заменяются на 0. Замены проводятся
in-place.

Проходимся по матрице. Если элемент равен 0, то ставим переменную zero_row
на True (чтобы в дальнейшем заменить эту строчку на строчку из нулей),
добавляем столбец в сет столбцов, которые должны стать нулями. Также
проходимся по уже пройденным строкам и заменяем значения в нужном столбце
на 0. Если встречаем индекс столбца из zero_cols, то присваиваем элементу
значение 0.

Лучшее решение: 2 ms, 18.57 Mb
"""


class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_cols = set()
        for i in range(m):
            zero_row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row = True
                    zero_cols.add(j)
                    for back in range(i - 1, -1, -1):
                        matrix[back][j] = 0
                if j in zero_cols:
                    matrix[i][j] = 0
            if zero_row:
                matrix[i] = [0] * n


if __name__ == '__main__':
    res = Solution()
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    res.setZeroes(matrix=matrix)
    for row in matrix:
        print(' '.join(map(str, row)))
