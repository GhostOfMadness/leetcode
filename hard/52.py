"""
N-Queens II.

Найти количество способов разместить N ферзей на поле N * N так, чтобы они
не били друг друга.

Пояснение:
- self.col[j]: True, если столбец j не занят, иначе False.
- self.main_diag[i + j]: True, если диагональ, сумма координат на которой
  равна i + j, не занята, иначе False.
- self.sup_diag[i - j]: True, если диагональ, разность координат на которой
  равна i - j, не занята, иначе False. Отрицательная разность работает,
  так как в этом случае смотрятся значения с правой стороны массива.

Пробуем ставить ферзя в свободный столбец новой строки и запускаем рекурсию.
Если все ферзи расставлены, то увеличиваем ответ на 1. После рекурсии
освобождаем занятое место.

Лучшее решение: 3 ms, 17.71 Mb
"""


class Solution:

    ans: int = 0

    def rec(self, size: int, left: int, i: int) -> None:
        if left == 0:
            self.ans += 1
        else:
            for j in range(size):
                cnd = (
                    self.col[j]
                    and self.main_diag[i + j]
                    and self.sup_diag[i - j]
                )
                if cnd:
                    self.col[j] = False
                    self.main_diag[i + j] = False
                    self.sup_diag[i - j] = False
                    self.rec(size=size, left=left-1, i=i+1)
                    self.col[j] = True
                    self.main_diag[i + j] = True
                    self.sup_diag[i - j] = True

    def totalNQueens(self, n: int) -> int:
        self.col = [True] * n
        self.main_diag = [True] * (2 * n - 1)
        self.sup_diag = [True] * (2 * n - 1)
        self.rec(size=n, left=n, i=0)
        return self.ans


if __name__ == '__main__':
    res = Solution()
    print(res.totalNQueens(n=8))
