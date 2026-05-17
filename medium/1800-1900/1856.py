"""
Maximum Subarray Min-Product.

Дан массив целых положительных чисел nums. Для любого подмассива min_prod
определяется как произведение минимального числа в подмассиве на сумму всех
элементов подмассива. Найти максимальное значение min_prod среди всех
подмассивов nums.

Идея в том, чтобы рассматривать каждое значение в массиве как минимум на
некотором подмассиве. Тогда подмассивом будет набор элементов слева и справа,
которые не меньше текущего. То есть для расчета min_prod нужно эффективно
определять такие границы и считать сумму элементов в подмассиве. Для второго
пункта подходят префиксные суммы, так как позволяют быстро найти сумму
значений на отрезке по его границам. А для первого пункта будем использовать
стек, в котором будет хранить индексы. Новый элемент выталкивает из стека
все индексы, значения на которых больше текущего. То есть в стеке остаются
индексы неубывающей последовательности чисел. При выталкивании элемента
можно легко определить границы подмассива. Справа это будет индекс текущего
числа, так как выталкивание происходит меньшим элементом. Слева это будет
предыдущий индекс в стеке или 0, если стек пуст. Обе эти границы в сам отрезок
не включаются, правая сдвигается на 1 влево, а левая - на 1 вправо. По
полученным границам находим сумму элементов и умножаем ее на значение на
выталкиваемом индексе. При необходимости обновляем ответ.

Лучшее решение: 195 ms (81.11%), 32.94 Mb (90.40%)
#stack #prefix_sum #array
"""


class Solution:

    def get_prefix_sum(self, nums: list[int], n: int) -> list[int]:
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        return prefix

    def get_min_prod(
        self,
        stack: list[int],
        prefix: list[int],
        nums: list[int],
        right: int,
    ) -> int:
        idx = stack.pop()
        val = nums[idx]
        if stack:
            last_idx = stack[-1]
        else:
            last_idx = -1
        min_prod = val * (prefix[right] - prefix[last_idx + 1])
        return min_prod

    def maxSumMinProduct(self, nums: list[int]) -> int:
        mod = 10 ** 9 + 7
        ans = 0
        n = len(nums)
        stack = []
        prefix = self.get_prefix_sum(nums, n)
        for i in range(n):
            num = nums[i]
            while stack and num < nums[stack[-1]]:
                min_prod = self.get_min_prod(stack, prefix, nums, i)
                if min_prod > ans:
                    ans = min_prod
            stack.append(i)
        while stack:
            min_prod = self.get_min_prod(stack, prefix, nums, n)
            if min_prod > ans:
                ans = min_prod
        return ans % mod
