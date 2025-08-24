"""
Combination Sum.

Дан список целых чисел candidates (числа в нем не повторяются) и целое число
target. Необходимо вывести список всех уникальных комбинаций чисел, сумма
которых дает target. Каждое число может быть использовано любое кол-во раз
в комбинации. Порядок следования чисел в комбинации не имеет значения,
то есть [2, 2, 3] == [2, 3, 2] == [3, 2, 2], это одна и та же комбинация.

Так как допустимы повторения чисел, то при каждом запуске рекурсии проходимся
циклом от текущего индекса до конца списка. В текущую комбинацию добавляем
новое число, обновляем ее сумму и продолжаем собирать комбинацию, пока ее
сумма не больше target. Если сумма стала равна target, то заносим полученную
комбинацию в ответ. После запуска рекурсии убираем последнее добавленное число
и добавляем следующее.

Лучшее решение: 10 ms, 17.77 Mb
"""


class Solution:

    def rec(self, comb: list[int], curr_sum: int, idx: int) -> None:
        if curr_sum == self.target:
            self.ans.append([e for e in comb])
        elif curr_sum < self.target:
            for i in range(idx, self.cnt):
                comb.append(self.candidates[i])
                curr_sum += self.candidates[i]
                self.rec(comb, curr_sum, i)
                comb.pop()
                curr_sum -= self.candidates[i]

    def combinationSum(
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        self.ans = []
        self.candidates = candidates
        self.target = target
        self.cnt = len(candidates)
        self.rec(comb=[], curr_sum=0, idx=0)
        return self.ans
