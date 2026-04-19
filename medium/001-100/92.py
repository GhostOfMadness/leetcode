"""
Reverse Linked List II.

Дан односвязный список и границы интервала left и right. Необходимо развернуть
этот интервал внутри списка.

Под разворотом интервала понимаем перенаправление ссылок внутри него. При этом
важно вписать обновленный интервал внутрь остального списка. Для этого нужно
знать первый элемент до начала интервала и первый элемент после него. Сначала
определяем before и start - первый элемент до интервала и первый элемент
интервала. Определяем prev и curr как первый и второй элементы интервала.
curr может быть равен None, но prev - обязательно узел, так как список не
может быть пустым. Идем по интервалу и разворачиваем ссылки next со следующего
на предыдущий элемент. После цикла prev - последний элемент исходного
интервала, а curr - первый элемент после интервала.

Теперь нужно вписать новый интервал в список. Если before = None, то перед
интервалом не было других элементов, значит prev теперь будет началом списка.
Если before - узел списка, то head остается началом списка, а к before
цепляется prev (before.next = prev). Значение curr не имеет значения, в любом
случае выполняем start.next = curr.

Лучшее решение: 0 ms, 19.05 Mb
#linked_list
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        values = []
        while self:
            values.append(self.val)
            self = self.next
        return ' -> '.join(map(str, values))


class Solution:

    def create_list(self, arr: list[int]) -> ListNode:
        if not arr:
            return None
        head = ListNode(val=arr[0])
        prev = head
        for i in range(1, len(arr)):
            node = ListNode(val=arr[i])
            prev.next = node
            prev = node
        return head

    def reverseBetween(
        self,
        head: ListNode,
        left: int,
        right: int,
    ) -> ListNode:
        before, start = None, head
        for _ in range(left - 1):
            before, start = start, start.next
        prev = start
        curr = start.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        start.next = curr
        if before:
            before.next = prev
            return head
        return prev
