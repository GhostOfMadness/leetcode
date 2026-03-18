"""
Count Submatrices with Top-Left Element and Sum Less Than K.

Дана матрица целых неотрицательных чисел размера n * m. Найти количество
подматриц, верхний левый угол которых находится в элементе на позиции (0, 0),
а сумма всех элементов не превышает заданное число k.

Так как все подматрицы начинаются в одном элементе, то можно последовательно
идти по строкам, наращивать суммы и увеличивать ответ на 1, если новая сумма
не больше k. Для нахождения суммы подматрицы (0, 0) - (i, j) нужно знать суммы
для подматриц с правым нижним углом в (i, j - 1), (i - 1, j), (i - 1, j - 1).
Тогда val = S(i, j - 1) + S(i - i, j) - S(i - 1, j - 1) + grid[i, j]. Можно
хранить полную матрицу таких сумм, но для расчета текущего нужно знать лишь
текущую и предыдущую строки, поэтому ограничимся ими. Также к этим строкам
матрицы префиксных сумм слева добавим ноль, чтобы и первый элемент считался
по общему алгоритму.

Можно идти по каждой строке до конца, а можно немного ускорить решение. Все
числа неотрицательные, значит, если на каком-то индексе j сумма стала больше
k, то дальше идти вправо смысла нет. И это верно для всех строк после текущей,
ведь числа снизу точно не уменьшат эту сумму. То есть для строки i + 1 хватит
движения до найденного right = j. Если в какой-то момент right стало равно 0,
то уже первый элемент новой строки делает сумму слишком большой. Значит нет
смысла идти не только вправо, но и вниз. В этом случае выходим из цикла.
Хотя на случайных тестах такой подход выгоды не дает, время даже чуть больше,
чем у варианта с проходом по всем строкам. Но если установить k на небольшое
значение, то такое сокращение операций дает заметный эффект.

Лучшее решение: 175 ms, 53.68 Mb
#array #matrix #prefix_sum
"""
import random

from test_class import Test


class Solution(Test):

    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        right = m
        prev = [0] * (right + 1)
        ans = 0
        for i in range(n):
            curr = [0] * (right + 1)
            for j in range(right):
                val = prev[j + 1] + curr[j] - prev[j] + grid[i][j]
                curr[j + 1] = val
                if val > k:
                    right = j
                    break
                ans += 1
            if right == 0:
                break
            prev = curr
        return ans

    def countSubmatrices2(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        prev = [0] * (m + 1)
        ans = 0
        for i in range(n):
            curr = [0] * (m + 1)
            for j in range(m):
                val = prev[j + 1] + curr[j] - prev[j] + grid[i][j]
                curr[j + 1] = val
                if val > k:
                    break
                ans += 1
            prev = curr
        return ans

    def data_genr(self, **kwargs):
        grid = []
        for _ in range(1000):
            row = random.choices(range(1001), k=1000)
            grid.append(row)
        k = random.randint(1, 10 ** 6)
        return dict(grid=grid, k=k)


res = Solution()
res.time_test([res.countSubmatrices, res.countSubmatrices2], n_iter=10 ** 3)
