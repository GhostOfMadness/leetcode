"""
Maximum Difference Between Increasing Elements.

Найти максимальную разницу между nums[i] и nums[j] при условии, что i < j
и nums[i] < nums[j].

Лучшее решение: 0 ms, 17.87 Mb
"""


class Solution:

    def maximumDifference(self, nums: list[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        ans = 0
        for e in nums:
            if e < curr_min:
                ans = max(ans, curr_max - curr_min)
                curr_min = e
                curr_max = e
            curr_max = max(curr_max, e)
        ans = max(ans, curr_max - curr_min)
        return ans if ans else -1
