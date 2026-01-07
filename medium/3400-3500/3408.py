"""
Design Task Manager.

Написать класс TaskManager, который поддерживает следующие операции:
- Добавление новой задачи с указанным приоритетом заданному пользователю.
  Id задачи уникален среди всех пользователей.
- Изменить приоритет указанной задачи.
- Удалить указанную задачу.
- Найти задачу с наибольшим приоритетом среди всех пользователей. Если таких
  задач несколько, то задачу с наибольшим id. Вывести id пользователя,
  для которого определена эта задача.

Будем поддерживать 3 структуры:
- heap из пар (-приоритет задачи, -id задачи). По умолчанию создается бинарная
  мин. куча, поэтому добавляем минусы для работы с максимумами.
- словарь task_priority, где для каждой задачи храним приоритет.
- словарь task_user, где для каждой задачи указан пользователь.

При добавлении новой задачи заносим ее в словари и кучу. При изменении
приоритета задачи меняем его в task_priority и добавляем обновленнную пару в
кучу (без удаления старой). При удалении задачи удаляем ее id из словарей
task_priority и task_user, кучу оставляем в текущем состоянии. При поиске
задачи с наибольшим приоритетом сначала проверяем, что куча не пуста. Затем
забираем элемент с вершины кучи. Если задачи с таким номером нет в словарях
или ее приоритет не соответствует актуальному значению, то берем следующий
элемент. Повторяем процесс, пока куча не опустеет или пока не возьмем
актуальную пару. В первом случае возращаем -1 (задач нет), во втором случае
удаляем задачу из словарей и возвращаем id пользователя, к которому она
относилась. При таком подходе получается "ленивое" удаление данных, которое
происходит только при запросе задачи с максимальным приоритетом, поэтому
память расходуется неэффективно, но система работает быстро.

Лучшее решение: 446 ms, 111.38 Mb
#hash_table #heap #array
"""
import heapq


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.heap = []
        self.task_priority: dict[int, int] = dict()
        self.task_user: dict[int, int] = dict()
        for e in tasks:
            user, task, priority = e
            self.heap.append((-priority, -task))
            self.task_priority[-task] = -priority
            self.task_user[-task] = user
        heapq.heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.task_priority[-taskId] = -priority
        self.task_user[-taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.task_priority[-taskId] = -newPriority

    def rmv(self, taskId: int) -> None:
        self.task_priority.pop(-taskId)
        self.task_user.pop(-taskId)

    def execTop(self) -> int:
        if not self.heap:
            return -1
        priority, task = heapq.heappop(self.heap)
        while (
            self.heap
            and (
                task not in self.task_priority
                or self.task_priority[task] != priority
            )
        ):
            priority, task = heapq.heappop(self.heap)
        if task not in self.task_priority:
            return -1
        self.task_priority.pop(task)
        self.task_user.pop(task)
        return self.task_user[task]
