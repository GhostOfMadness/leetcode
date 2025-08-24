"""
Permutations.

Необходимо получить массив всех перестановок исходного массива целых чисел.

Аргументы функции rec:
- left_set - множество еще не использованных чисел.
- perm - текущая перестановка.

Если не использованных чисел нет, то добавляем перестанвку в ответ. В ином
случае, для каждого числа в left_set запускаем рекурсию, убирая из left_set
текущее число и добавляя его в перестановку.

Лучшее решение: 0 ms, 17.92 Mb
"""


class Solution:

    def rec(
        self,
        left_set: set[int],
        perm: list[int] = [],
    ) -> None:
        if not left_set:
            self.ans.append([e for e in perm])
        else:
            for e in left_set:
                self.rec(left_set - {e}, perm + [e])

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        self.rec(left_set=set(nums))
        return self.ans


if __name__ == '__main__':
    res = Solution()
    nums = [1, 2, 3]
    print(res.permute(nums))
