"""
Convert Sorted Array to Binary Search Tree.

Необходимо преобразовать отсортированный по возрастанию массив целых чисел в
сбалансированное бинарное дерево поиска.

Так как массив отсортирован, то корнем дерева точно будет элемент в его центре.
Если длина массива четная, то можно брать любой из пары элементов, высота
поддеревьев будет отличаться не более чем на 1. Корнями левого и правого
поддеревьев будут элементы в середине подмассивов слева и справа от найденного
корня. Далее этот процесс повторяется. Таким образом, на каждом шаге мы сначала
находим середину подмассива в заданных границах, получая значения корня
поддерева, и запускаем рекурсию от левой (от left до mid) и правой (от mid + 1
до right) частей массива для определения левого и правого потомка. Если
left == right, то подмассив уже не делится, потомка нет, поэтому возвращаем
None.

Лучшее решение: 0 ms, 20.22 Mb
#binary_seacrh_tree #divide_and_conquer
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rec(self, nums: list[int], left: int, right: int) -> TreeNode:
        if left == right:
            return None
        mid = (left + right) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.rec(nums, left, mid)
        node.right = self.rec(nums, mid + 1, right)
        return node

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        left, right = 0, len(nums)
        return self.rec(nums, left, right)
