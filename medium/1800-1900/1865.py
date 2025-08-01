"""
Finding Pairs With a Certain Sum.

Необходимо реализовать класс FindSumPairs на основе двух массивов целых
чисел. В классе определены 2 операции:
- add(index, val) - добавить к элементу nums2[index] значение val.
- count(tot) - найти количество пар индексов i и j, которые удовлетворяют
  равенству nums1[i] + nums2[j] = tot.

Лучшее решение: 154 ms, 48.86 Mb
"""
from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1_cnt = Counter(nums1)
        self.nums2 = nums2
        self.nums2_cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_cnt[self.nums2[index]] -= 1
        if not self.nums2_cnt[self.nums2[index]]:
            self.nums2_cnt.pop(self.nums2[index])
        self.nums2[index] += val
        self.nums2_cnt[self.nums2[index]] = (
            self.nums2_cnt.get(self.nums2[index], 0)
            + 1
        )

    def count(self, tot: int) -> int:
        acc = 0
        for k, v in self.nums1_cnt.items():
            target = tot - k
            if target in self.nums2_cnt:
                acc += v * self.nums2_cnt[target]
        return acc
