"""
Delete Nodes From Linked List Present in Array.

Удалить из связного списка все узлы, значения которых находятся в массиве nums.

Сначала создаем множество из массива nums для ускорения поиска. Затем сдвигаем
указатель головы списка на первый узел, значение которого не находится во
множестве (по условию задачи есть минимум один такой узел), и удаляем ссылку
на него с предыдущего узла, если такой есть (может быть, что голова списка
не сдвинется). После этого проходимся по всем последующим узлам, поддерживая
указатели на текущий и предыдущий узлы. Если значение текущего узла есть во
множестве, то предыдущий узел будет ссылаться на потомка текущего узла, при
этом ссылка на предыдущий узел не сдвигается. В ином случае, указатель
предыдущего узла сдвигается на текущий узел.

Лучшее решение: 38 ms, 59.32 Mb
#linked_list #hash_table
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        nums_set = set(nums)
        root = head
        prev = None
        while root.val in nums_set:
            root = root.next
        if prev:
            prev.next = None
        curr = root.next
        prev = root
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return root
