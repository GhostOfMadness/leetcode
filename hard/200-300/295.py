"""
Find Median from Data Stream.

Необходимо реализовать класс MedianFinder, который позволяет эффективно
добавлять элементы в структуру и возвращать медиану переданных значений.

Используем 2 кучи. heapMin - двоичная мин-куча, отвечающая за правую часть
массива, heapMax - двоичная макс-куча для левой части массива. При этом размер
heapMax либо равен размеру heapMin, либо на 1 превышает его. При таком условии
медиана находится на вершине heapMax, если размеры куч не равны, или считается
как среднее из heapMax[0] и heapMin[0] в случае равенства. То есть поиск
медианы занимает O(1).

Добавление элемента в кучу занимает O(log(heap.size)). Важно понять, куда и
что добавить. Если размеры куч совпадают (за это отвечает flag = True), то
какой-то элемент нужно добавить в heapMax, чтобы поддерживать заданное
соотношение размеров. Если num <= heapMax[0], то нужно добавить num, иначе
- нужно добавить heapMin[0] в heapMax, а num в heapMin. Для реализации этой
логики добавляем num в heapMin, а затем heapMin[0] кладем в heapMax. Если num
изначально должен был быть добавлен в heapMax, то он окажется на вершине
heapMin и заберем именно его, иначе - num просеится вниз и окажется на нужном
месте в heapMin. Если размеры куч не совпадают, то элемент нужно добавить в
heapMin. Это будет либо num, либо элемент с вершины heapMax, если num должен
уйти в левую часть массива. Действуем аналогично прошлой ситуации. Добавляем
num в heapMax, а heapMax[0] кладем в heapMin. После любого добавления меняем
значение флага на противоположное.

Лучшее решение: 122 ms, 42.04 Mb
#heap
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.heapMin = []
        self.heapMax = []
        heapq.heapify(self.heapMin)
        heapq.heapify_max(self.heapMax)
        self.flag = True

    def addNum(self, num: int) -> None:
        if self.flag:
            heapq.heappush_max(
                self.heapMax,
                heapq.heappushpop(self.heapMin, num),
            )
        else:
            heapq.heappush(
                self.heapMin,
                heapq.heappushpop_max(self.heapMax, num),
            )
        self.flag = not self.flag

    def findMedian(self) -> float:
        if self.flag:
            return (self.heapMax[0] + self.heapMin[0]) / 2
        return self.heapMax[0]
