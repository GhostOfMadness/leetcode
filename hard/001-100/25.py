"""
Reverse Nodes in k-Group.

Дан односвязный список, состоящий не более чем из 5000 узлов. Необходимо
развернуть каждые k последовательных узлов списка. Если осталось меньше k
узлов, то оставить их в исходном порядке. Например:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 9 -> 8 -> 7 -> 10

Сначала определим функцию reverse_section, которая будет разворачивать один
фрагемент, начиная от переданного узла root. В start сохраняем исходное
начало списка, которое после разворота станет концом. Заводим счетчик шагов
и разворачиваем фрагмент, то есть ставим ссылку next не на следующий узел,
а на предыдущий. Повторяем это действие, пока не дойдем до конца списка или
пока не сделаем k - 1 шаг. Возвращаем кортеж из 4-х элементов:
- 1: конец развернутого списка (prev)
- 2: начало развернутого списка
- 3: начало следующего фрагмента (root)
- 4: сделанное количество шагов (step)

Если сделали не все шаги, то длина развернутого фрагмента была меньше k,
то есть нужно развернуть его обратно. Для этого вызываем reverse_section
от начала этого фрагмента (start) и сделанного числа шагов (step). Затем
добавлеем начало развернутого фрагмента к концу уже собранных вместе
фрагментов и меняем указатель на конец.

Лучшее решение: 0 ms, 18.48 Mb
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

    def reverse_section(self, root: ListNode, k: int):
        start = root
        step = 0
        prev = None
        while root and step < k:
            next_node = root.next
            root.next = prev
            prev = root
            root = next_node
            step += 1
        return (prev, start, root, step)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = head
        prev_start = ListNode()
        to_add = prev_start
        while root:
            start, end, root, step = self.reverse_section(root, k)
            if step < k:
                start, end, root, step = self.reverse_section(start, step)
            to_add.next = start
            to_add = end
        return prev_start.next
