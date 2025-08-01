"""
Pascal's Triangle.

Сгенерировать первые numRows строк треугольника Паскаля.

В начале и конце каждой строки стоят единицы, а остальные значения равны
сумме 2-х элементов, расположенных над текущей позицией в предыдущей строчке.

Лучшее решение: 0 ms, 17.72 Mb
"""


class Solution:

    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for i in range(numRows):
            ans.append(
                [
                    1
                    if j == 0 or j == i
                    else ans[-1][j] + ans[-1][j - 1]
                    for j in range(i + 1)
                ]
            )
        return ans
