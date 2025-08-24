"""
LRU Cache.

Необходимо реализовать кеш по принципу LRU, то есть при отсутствии свободного
места из кеша удаляется ключ с самым ранним временем обращения.

Так как нужен быстрый доступ по ключу, то будем использовать словарь. Также
необходимо быстро находить ключ, который нужно удалить. Для этой цели будем
использовать двусвязный список, каждый узел которого будет хранить ключ,
значение и ссылки на соседей.

Параметры LRUCache:
- d - словарь из пар "ключ - узел".
- start - ссылка на узел, который можно удалить.
- end - ссылка на последний использованный узел.
- capacity - вместимость кеша.
- size - текущее количество элементов в кеше.

Метод get обращается к кешу по ключу и возвращает его значение, если ключ
есть, или -1, если его нет. В случае, когда ключ есть в кеше, соответствующий
ему узел необходимо сдвинуть в конец списка. Для этого реализуем функцию
__move_to_end(). Так как мы "извлекаем" элемент, то его соседи справа и слева
должны будут ссылаться друг на друга. Для текущего узла node предыдущим
станет узел self.end, а следующим - None. Также для узла self.end меняем
ссылку на следующий элемент с None на node и ставим self.end на node. Функция
запускается только, когда текущий узел не равен self.end, значит сосед справа
точно есть. Если соседа слева нет, то есть node = self.start, то сдвигаем
указатель self.start.

Метод put добавляет элемент в кеш. Если ключ уже есть в кеше, то переписываем
его значения и сдвигаем соответствующий узел в конец. Если ключа нет, а кеш
заполнен не полностью, то создаем новый узел и ставим его в конец. Если кеш
заполнен полностью, то также добавлем новый узел в конец, но при этом удалем
ключ узла self.start и сдвигаем указатель self.start на следующее значение.

Лучшее решение: 119 ms, 78.03 Mb
"""


class ListNode:

    def __init__(
        self,
        val: int,
        key: int,
        prev=None,
        next=None,
    ):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return ' -> '.join(map(str, res))


class LRUCache:

    def __init__(self, capacity: int):
        self.d: dict[int, ListNode] = dict()
        self.start: ListNode | None = None
        self.end: ListNode | None = None
        self.capacity: int = capacity
        self.size: int = 0

    def __move_node_to_end(self, node: ListNode):
        if node.key != self.end.key:
            if node.key == self.start.key:
                self.start = self.start.next
            else:
                node.prev.next = node.next
            node.next.prev = node.prev
            self.end.next = node
            node.prev = self.end
            node.next = None
            self.end = node

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.__move_node_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.__move_node_to_end(node)
        elif self.size < self.capacity:
            node = ListNode(val=value, key=key, prev=self.end, next=None)
            self.d[key] = node
            if not self.size:
                self.start = node
            else:
                self.end.next = node
            self.end = node
            self.size += 1
        else:
            node = ListNode(val=value, key=key, prev=self.end, next=None)
            self.d[key] = node
            self.end.next = node
            self.end = node
            self.d.pop(self.start.key)
            self.start = self.start.next
            self.start.prev = None
