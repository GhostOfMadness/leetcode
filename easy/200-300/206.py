"""
Reverse Linked List.

Дан односвязный список. Необходимо развернуть его и вернуть начало списка.

Идем по узлам списка и меняем направление ссылок на противоположное.

Лучшее решение: 0 ms, 20.39 Mb
#linked_list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev
