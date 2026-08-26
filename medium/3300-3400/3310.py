"""
Remove Methods From Project.

В проекте используются n методов, пронумерованных от 0 до n - 1. Даны целые
числа n и k, а также массив invocations, invocations[i] = [a, b], то есть
метод a вызывает метод b. В методе под номером k есть известный баг. Все
методы, которые вызываются им, напрямую или нет, считаются подозрительными.
Нужно удалить эту группу подозрительных методов и вернуть список номеров
методов, которые останутся. Если есть какой-либо метод за пределами этой
группы, который вызывает любой метод из группы, то удаление невозможно,
поэтому возвращаем номера всех методов.

По сути дан ориентированный граф без петель и кратных ребер. Исходный массив
invocations переделываем в список смежности и сохраняем в массиве arr. С
помощью поиска в ширину идем от вершины k и в массиве visited помечаем все
вершины, которые вызываются этим методом. Теперь нужно выяснить, есть ли
хотя бы одно ребро из непомеченной вершины в помеченную. Для этого проверяем
пары в массиве invocations и сохраняем результат в переменной status. Если
такое ребро есть, то есть status = True, то удалить группу нельзя, поэтому
возвращаем список всех методов. В ином случае, заносим в ответ все
непомеченные вершины.

Лучшее решение: 275 ms (75.76%), 98.67 Mb (100%)
#bfs #graph_theory
"""
from collections import deque


class Solution:

    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: list[list[int]],
    ) -> list[int]:
        arr = [[] for _ in range(n)]
        for e in invocations:
            a, b = e
            arr[a].append(b)
        visited = [False] * n
        q = deque([k])
        while q:
            e = q.popleft()
            visited[e] = True
            for v in arr[e]:
                if not visited[v]:
                    q.append(v)       
        status = any(not visited[e[0]] and visited[e[1]] for e in invocations)
        if status:
            return list(range(n))
        return [i for i in range(n) if not visited[i]]
