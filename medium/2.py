"""
Add Two Numbers.

Два числа записаны в обратном порядке (от младших разрядов к старшим)
и представлены в виде односвязных списков. Необходимо вернуть их сумму
в таком же формате.

Складываем списки поэлементно (как столбиком). В переменной add хранится 1,
если предыдущая сумма была больше 9, иначе - 0.

Лучшее решение: 3 ms, 17.89 Mb
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        num = []
        while self:
            num.append(self.val)
            self = self.next
        return ' -> '.join(map(str, num))


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(val=(l1.val + l2.val) % 10)
        add = l1.val + l2.val >= 10
        l1 = l1.next
        l2 = l2.next
        prev = start
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            node = ListNode(val=(l1_val + l2_val + add) % 10)
            prev.next = node
            prev = node
            add = l1_val + l2_val + add >= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if add:
            node = ListNode(val=int(add))
            prev.next = node
        return start
