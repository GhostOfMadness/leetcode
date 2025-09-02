"""
Merge Two Sorted Lists.

Объединить 2 связных списка, отсортированных по возрастанию, в один.

Запускаем цикл, пока хотя бы один из узлов не пуст. Если второй список
пуст или значение в первом списке не пустое и меньше значения из второго
списка, то добавляем в объединенный список узел из списка 1 и сдвигаем
указатель на этом списке. В ином случае, берем узел из списка 2.

Лучшее решение: 0 ms, 17.67 Mb
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return ' -> '.join(map(str, res))


class Solution:

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        root = None
        curr = None
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                if not root:
                    root = list1
                    curr = list1
                else:
                    curr.next = list1
                    curr = list1
                list1 = list1.next
            else:
                if not root:
                    root = list2
                    curr = list2
                else:
                    curr.next = list2
                    curr = list2
                list2 = list2.next
        return root
