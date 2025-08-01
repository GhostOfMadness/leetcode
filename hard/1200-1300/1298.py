"""
Maximum Candies You Can Get From Boxes.

Каждая коробка может быть открытой изи закрытой. Кроме того, в каждой могут
находиться конфеты, ключи к другим коробкам и другие коробки. По данному
исходному набору коробок определить, какое количество конфет можно из них
достать.

Лучшее решение: 12 ms, 27.86 Mb
"""


from collections import deque


class Solution:

    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        acc = 0
        q = deque(box for box in initialBoxes if status[box])
        can_visit = [False] * len(status)
        for box in initialBoxes:
            if not status[box]:
                can_visit[box] = True
        while q:
            box = q.popleft()
            acc += candies[box]
            for k in keys[box]:
                status[k] = 1
                if can_visit[k]:
                    q.append(k)
                    can_visit[k] = False
            for b in containedBoxes[box]:
                if status[b]:
                    q.append(b)
                else:
                    can_visit[b] = True
        return acc
