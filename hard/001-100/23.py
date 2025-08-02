"""
Merge k Sorted Lists.

Необходимо объединить k отсортированных по возрастанию связных списков в один,
также отсортированный по возрастанию.

Списки отсортированы по возрастанию, значит первое значение точно хранится
в начале одного из них. Его можно найти с помощью функции min для первых
элементов списков. Затем сделать начало этого списка головой общего списка,
а в массиве заменить извлеченный узел следующим за ним. Но на следующей
итерации снова бы пришлось проходиться по k значениям и искать минимум,
что довольно долго.

Поэтому воспользуемся кучей, где минимум всегда находится на вершине. Куча
состоит из кортежей вида (значение (val), индекс в lists). Пока куча не пуста,
извлекаем минимальный элемент, берем его индекс idx и сохраняем соотвествующий
ему узел lists[idx] в node. В исходном списке на место lists[idx] ставим
следующий за ним и, если его значение отлично от None, добавляем его в кучу.
То есть куча состоит только из числовых значений и ее размер не больше k.
node становится следующим элементом для curr, если это не первый элемент
общего списка, иначе head = node. После этого ставим curr на node.

Лучшее решение: 4 ms, 20.30 Mb
"""


import heapq


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nums = []
        while self:
            nums.append(self.val)
            self = self.next
        return ' -> '.join(map(str, nums))


class Solution:

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        head = None
        curr = None
        while heap:
            idx = heapq.heappop(heap)[1]
            node = lists[idx]
            lists[idx] = node.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            if not head:
                head = node
            else:
                curr.next = node
            curr = node
        return head
