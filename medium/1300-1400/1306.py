"""
Jump Game III.

Дан массив целых чисел arr, 0 <= arr[i] < arr.length. С текущей позиции i
можно перейти на  позицию i - arr[i] или i + arr[i], если эти позиции лежат в
пределах массива. Начальная позиция задается перменной start. Определить,
можно ли с начальной позиции попасть на любой индекс i, где arr[i] == 0.

Для решения можно использовать поиск в ширину или в глубину. В обоих случаях
сначала создаем массив visited, где будем отмечать уже посещенные индексы,
чтобы не проверять одну позицию несколько раз. При поиске в ширину индексы
для проверки кладутся в очередь. На каждом шаге берем первый элемент очереди
и помечаем его посещенным. Если значение на этой позиции равно 0, то возвращаем
True. Если нет, то добавляем в конец очереди непосещенные индексы для ходов
влево и вправо, если они находятся в пределах массива. Если очередь опустела
и функция еще ничего не вернула, то 0 недостижим, поэтому возвращаем False.
Вместо очереди можно формировать новый слой и затем перекидывать ссылку на
этот новый массив.

Поиск в глубину работает по этому же принципу, только вместо очереди используем
стек и на каждом шаге снимаем элемент с вершины. Новые значения также кладутся
в конец, поэтому как бы идем по ветке бинарного дерева.

Оба подхода работают одинаково по времени, dfs чуть-чуть быстрее.

Лучшее решение (dfs): 3 ms (99.94%), 25.17 Mb (92.68 Mb)
#array #dfs #bfs
"""


class Solution:


    def canReach_dfs(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        q = [start]
        while q:
            idx = q.pop()
            visited[idx] = True
            num = arr[idx]
            if num == 0:
                return True
            left = idx - num
            right = idx + num
            if left >= 0 and not visited[left]:
                q.append(left)
            if right < n and not visited[right]:
                q.append(right)            
        return False

    def canReach_bfs(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        q = [start]
        while q:
            new = []
            for idx in q:
                visited[idx] = True
                num = arr[idx]
                if num == 0:
                    return True
                left = idx - num
                right = idx + num
                if left >= 0 and not visited[left]:
                    new.append(left)
                if right < n and not visited[right]:
                    new.append(right)
            q = new
        return False
