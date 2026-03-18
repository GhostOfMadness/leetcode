"""
Special Positions in a Binary Matrix.

Дана бинарная матрица размера m * n. Найти количество позиций (i,j) таких, что
mat[i][j] == 1, а все остальные значения в i-й строке и j-м столбце равны 0.

Создадим массивы cols и rows: cols[j] - количество единиц в j-м столбце,
rows[i] - -1, если в строке нет единиц или их количество больше 1, индекс
столбца j, если единица ровно одна. Проходимся по матрице и заполняем массивы.
Затем порходим по массиву rows. Если значение не равно -1, то проверяем, что
cols[rows[i]] == 1. Если это так, то добавляем 1 к ответу.

Лучшее решение: 3 ms, 19.88 Mb
#matrix #array
"""


class Solution:

    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cols = [0] * n
        rows = [-1] * m
        for i in range(m):
            idx = None
            cnt = 0
            for j in range(n):
                if mat[i][j]:
                    idx = j
                    cnt += 1
                    cols[j] += 1
            if cnt == 1:
                rows[i] = idx
        return sum(cols[e] == 1 for e in rows if e != -1)
