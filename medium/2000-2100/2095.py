"""
Delete the Middle Node of a Linked List.

Дан односвязный список длины n. Необходимо удалить его центральный элемент
и вернуть начало измененного списка. Если n - четное число, то нужно удалить
узел n // 2 при нумерации с нуля.

Используем метод двух указателей. Первый указатель "черепаха" будет проходить
один узел за ход, указатель "заяц" - 2 узла за ход. Цикл идет, пока "заяц"
указывает на какой-то узел у которого есть сосед справа. При таком подходе
к завершению цикла "черепаха" будет указывать на тот узел, который нужно
удалить. Так как список односвязный, то это не очень удобно, так как нельзя
вернуться к предыдущему узлу. Для решения этой проблемы можно добавить
дополнительный узел в начало и запускать "черепаху" из него. Или можно
поддерживать еще один указатель на элемент перед удаляемым, или можно
стартовать с None, но добавить обработку этого случая через if-else, чтобы
корректно переходить на следующий узел. По времени работы лучшим оказывается
вариант с дополнительным узлом, так как не нужны дополнительные проверки
и присваивания значений, но требуется дополнительная память на узел. Из
других вариатов эффективнее подход с тремя указателями без лишних проверок.

Лучшее решение (по времени): 67 ms (93.52 %), 63.47 Mb (5.52%)
Лучшее решение (по памяти): 83 ms (72.08%), 62.29 Mb (77.79%)
#linked_list #two_pointers
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        arr = []
        while self:
            arr.append(self.val)
            self = self.next
        return ' -> '.join(map(str, arr))


class Solution:

    def deleteMiddleWithAddNode(self, head: ListNode) -> ListNode:
        node = ListNode(val=0)
        node.next = head
        fast = head
        slow = node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if slow.val == 0:
            return None
        slow.next = slow.next.next
        return head

    def deleteMiddleThreePointers(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow, prev = slow.next, slow
        if not prev:
            return None
        prev.next = prev.next.next
        return head  
