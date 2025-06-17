"""
N-Queens.

Найти количество способов разместить N ферзей на поле N * N так, чтобы они
не били друг друга.

Пояснение:
- self.col[j]: True, если столбец j не занят, иначе False.
- self.main_diag[i + j]: True, если диагональ, сумма координат на которой
  равна i + j, не занята, иначе False.
- self.sup_diag[i - j]: True, если диагональ, разность координат на которой
  равна i - j, не занята, иначе False. Отрицательная разность работает,
  так как в этом случае смотрятся значения с правой стороны массива.
- curr - текущее состояние поля.

Пробуем ставить ферзя в свободный столбец новой строки и запускаем рекурсию.
Если все ферзи расставлены, то добавляем полученную комбинацию в ответ.
После рекурсии освобождаем занятое место.

Лучшее решение: 7 ms, 18.37 Mb
"""


class Solution:

    def rec(
        self,
        size: int,
        left: int,
        i: int,
        curr: list[list[str]],
        ans: list[list[list[str]]],
    ) -> None:
        if left == 0:
            ans.append([''.join(e) for e in curr])
        else:
            for j in range(size):
                cnd = (
                    self.col[j]
                    and self.main_diag[i + j]
                    and self.sup_diag[i - j]
                )
                if cnd:
                    curr[i][j] = 'Q'
                    self.col[j] = False
                    self.main_diag[i + j] = False
                    self.sup_diag[i - j] = False
                    self.rec(size=size, left=left-1, i=i+1, curr=curr, ans=ans)
                    curr[i][j] = '.'
                    self.col[j] = True
                    self.main_diag[i + j] = True
                    self.sup_diag[i - j] = True

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.col = [True] * n
        self.main_diag = [True] * (2 * n - 1)
        self.sup_diag = [True] * (2 * n - 1)
        curr = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.rec(size=n, left=n, i=0, curr=curr, ans=ans)
        return ans
