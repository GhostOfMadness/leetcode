"""
Convert Binary Number in a Linked List to Integer.

Число в двоичной записи хранится в виде связного списка, самый значащий бит
находится в голове списка. Необходимо перевести это число в десятичную запись.

Идем до конца списка, умножая предыдущий ответ на 2 и прибавляя текущий бит.

Лучшее решение: 0 ms, 17.88 Mb
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
