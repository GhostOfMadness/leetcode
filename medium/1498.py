"""
Number of Subsequences That Satisfy the Given Sum Condition.

Найти количество непустых подпоследовательностей, в которых сумма минимального
и максимального элементов не превышает заданное значение.

Пояснение к решению:
С помощью бинарного поиска находим первую позицию right таким образом, что
к текущему значению left можно добавить любую подпоследовательность из
[left + 1, right). Количество таких подпоследовательностей = сумма
биноминальных коэффициентов от 0 до длины [left + 1, right). Эта сумма
описывается функцией (1 + x) ** n, где x = 1 -> 2 ** n. Поэтому предварительно
насчитываем вохможные степени двойки. Далее используем метод двух указателей
и сдвигаем правую границу влево. Цикл завершается, когда долшли до конца
массива или текущее число больше половины target, а значит не может быть
использовано даже с самим собой.

Лучшее решение: 119 ms, 27.60 Mb
При замене цикла while на for: 116 ms, 27.80 Mb
"""


class Solution:

    mod: int = 10 ** 9 + 7

    def binsearch(
        self,
        nums: list[int],
        target: int,
        left: int,
        right: int,
    ) -> int:
        base = nums[left]
        mid = (left + right) // 2
        while left < right:
            if base + nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        return mid

    def numSubseq2(self, nums: list[int], target: int) -> int:
        nums.sort()

        if nums[0] * 2 > target:
            return 0

        size = len(nums)
        right = self.binsearch(nums, target, 0, size) - 1

        degrees = [1] * (right + 1)
        for i in range(1, right + 1):
            degrees[i] = (2 * degrees[i - 1]) % self.mod

        ans = degrees[right] % self.mod
        left = 1
        while left < size and nums[left] * 2 <= target:
            while nums[left] + nums[right] > target:
                right -= 1
            ans = (ans + degrees[right - left]) % self.mod
            left += 1
        return ans
