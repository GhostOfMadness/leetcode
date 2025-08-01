"""
Remove Nth Node From End of List.

Удалить n-й элемент из конца связного списка.

Устанавливаем текущее значение корня на начало списка, заводим левый указатель
и счетчик i. Так как мы не знаем размер списка, то не можем сразу сказать,
какой элемент нужно удалить. Поэтому фактически пойдем окном размера n + 2.
n + 2, так как цикл идет до получения None, то есть выйдет на 1 за границы
списка, а также нам нужно получить не сам удаляемый узел, а тот, что перед ним.
Внутри цикла на каждом шаге сдвигаем значение корня, а когда i станет больше
n, то сдвигаем и left. Таким образом, left будет указывать как раз на узел
перед удаляемым.

Если left так и остался равен None, то необходимо удалить первый узел. В этом
случае возвращаем следующий узел за head. В ином случае перекидываем ссылку
узла left на следующий элемент (если он есть) его правого соседа.

Лучшее решение: 0 ms, 17.74 Mb
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ans = []
        while self:
            ans.append(self.val)
            self = self.next
        return ' -> '.join(map(str, ans))


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = head
        left = None
        i = 1
        while root:
            if i > n:
                left = left.next if left else head
            root = root.next
            i += 1
        if not left:
            return head.next
        left.next = left.next.next if left.next else None
        return head

    def listify(self, arr: list[int]):
        root = ListNode(val=arr[0])
        curr = root
        for i in range(1, len(arr)):
            node = ListNode(val=arr[i])
            curr.next = node
            curr = node
        return root
