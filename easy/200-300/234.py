"""
Palindrome Linked List.

Проверить, является ли односвязный список полиндромом.

Лучшее решение (O(n) по памяти): 11 ms, 39.23 Mb
Лучшее решение (O(1) по памяти): 42 ms, 30.17 Mb
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        """Функция с O(n) по времени и памяти."""
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]

    def is_palindrome(self, head: ListNode) -> bool:
        """Функция с O(n) по времени и O(1) по памяти."""
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        half = size // 2
        i = 0
        prev_node = None
        curr = head
        while i < half:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
            i += 1
        if size % 2 == 1:
            curr = curr.next
        while curr:
            if prev_node.val != curr.val:
                return False
            prev_node = prev_node.next
            curr = curr.next
        return True
