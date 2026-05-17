"""
Rotate List.

Дано начало односвязного списка и целое неотрицательное число k. Необходимо
повернуть список на k позиций вправо, то есть переместить конец списка в
начало k раз.

Если список изначально пуст, то возвращаем None. В общем случае, сначала ищем
длину списка и сохраняем его конец в переменную tail. По условию k может быть
очень большим и превышать длину списка, поэтому берем остаток от деления k на
длину списка как кол-во шагов сдвига shift, чтобы исключить круговые повороты.
То есть shift последних элементов нужно переместить в начало, при этом связи
между этими элементами не меняются. Для выполнения этой операции нужно найти
новый хвост списка new_tail, это элемент с номером length - shift при
нумерации с 1. Следующий за ним узел будет новой головой списка new_head. Для
new_tail ставим параметр next на None, так как теперь это хвост, а сохраненный
ранее исходный конец списка tail связываем с исходной головой списка.

Лучшее решение: 0 ms (100%), 19.21 Mb (74.76 %)
#linked_list
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        shift = k % length
        if not shift:
            return head
        new_tail = head
        for _ in range(length - shift - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head
