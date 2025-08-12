"""
Swap Nodes in Pairs.

Дан связный список. Необходимо поменять местами каждую пару узлов, то есть
1 со 2, 3 с 4, и т.д. Менять только значения val нельзя.

Началомнового списка будет совпадать с головой старого списка, если этот
список пуст или состоит из одного элемента. В ином случае, это второй узел,
то есть head.next.

Идем по списку до тех пор, пока до конца минимум два узла. next_node - узел,
который идет за текущим (head). После обмена он должен идти перед текущим.
Поэтому head.next = next_node.next, next_node.next = head. Также необходимо
перекинуть ссылку с узла, который шел до этой пары (prev). После обмена
prev = head, head = head.next.

Лучшее решение: 0 ms, 17.63 Mb
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

    def swapPairs(self, head: ListNode) -> ListNode:
        root = head if not head or not head.next else head.next
        prev = None
        while head and head.next:
            next_node = head.next
            head.next = next_node.next
            next_node.next = head
            if prev:
                prev.next = next_node
            prev = head
            head = head.next
        return root

    def listify(self, arr: int) -> ListNode:
        if not arr:
            return None
        head = ListNode(val=arr[0])
        root = head
        for i in range(1, len(arr)):
            node = ListNode(val=arr[i])
            root.next = node
            root = node
        return head


if __name__ == '__main__':
    res = Solution()
    arr = []
    head = res.listify(arr)
    root = res.swapPairs(head)
    print(root)
