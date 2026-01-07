"""
Copy List with Random Pointer.

Дан односвязный список, в узлах которого помимо числового значения и ссылки
на следующий узел есть ссылка на случайный узел в списке. Необходимо создать
копию этого списка с сохранением структуры.

Создаем копию за 2 прохода по списку. На первом этапе заполняем словари
old_idx и idx_new. old_idx хранит пары "узел исходного списка - его индекс
в списке", idx_new - "индекс в списке - ссылка на узел нового списка". Здесь
на каждом шаге создаются новые узлы, копирующие значения исходных, которые
соединяются в одну последовательность через ссылки next.

На втором этапе определяем случайные указатели. Для этого проходимся по
ключам словаря old_idx. Если у исходного узла есть ссылка на случайный узел,
то через тот же словарь old_idx находим его позицию в списке. Затем нужно
копировать эту связь в новый список, для чего используем словарь idx_new.
idx_new[idx] - узел, к которому нужно добавить ссылку, idx_new[idx_random]
- узел, который нужно добавить.

Лучшее решение: 28 ms, 18.53 Mb
#linked_list #hash_table
"""


class Node:

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        new_head = Node(x=head.val)
        curr = head.next
        prev = new_head
        old_idx = {head: 0}
        idx_new = {0: new_head}
        idx = 1
        while curr:
            node = Node(x=curr.val)
            old_idx[curr] = idx
            idx_new[idx] = node
            prev.next = node
            prev = node
            curr = curr.next
            idx += 1
        for node, idx in old_idx.items():
            if node.random:
                idx_random = old_idx[node.random]
                idx_new[idx].random = idx_new[idx_random]
        return new_head
