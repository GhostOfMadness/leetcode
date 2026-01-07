"""
Design a Food Rating System.

Реализовать класс FoodRatings, который поддерживает 2 операции:
- Изменить значение рейтинга блюда.
- Вывести блюдо с наибольшим рейтингом для заданного типа кухни. Если таких
  несколько, то выбрать блюдо с лексиграфически наименьшим названием.

Вариант 1.
Используем дерево отрезков из пар (-1 * рейтинг, название блюда). Для каждого
типа кухни храним свой массив (словарь cuisine_arr), а также словарь, в
котором блюду сопоставляется его индекс в этом массиве (cuisine_food_idx).
Кроме того, в словаре food_cuisine храним пары "блюдо - тип кухни". При
инициализации объекта сначала заполняем эти словари, а также времененный
словарь cuisine_len, хранящий кол-во блюд данного вида кухни и позволяющий
быстро задавать индекс блюда в массиве. Когда данные занесены, переводим
массивы в деревья отрезков. Для этого каждый массив расширяем до ближайшей
степени двойки (число n) * 2 - 1. Переносим старые значения с индекса n - 1,
в это же время обновляем индексы блюд в cuisine_food_idx. Заполняем оставшиеся
значения минимумами из потомков. Таким образом, первым элементом нового
массива будет блюдо с наибольшим рейтингом и лексикографически меньшим
названием.

Метод highestRated работает за O(1), так как ответ всегда на 0-й позиции в
нужном массиве. Изменение рейтинга работает за O(logK), где K - размер дерева.
Получаем индекс блюда в массиве, меняем его рейтинг и обновляем значения его
предков.

Вариант 2.
Используем кучу. Для каждого типа кухни храним кучу из кортежей (-1 * рейтинг,
название блюда) (cuisine_heap), для каждого блюда - актуальный рейтинг
(food_rating) и тип кухни (food_cuisine). Проблема в том, что в куче нельзя
поменять элемент в произвольном месте массива. Поэтому при изменении рейтинга
будем только добавлять новую пару в кучу и обновлять значение в food_rating.
Удаление может происходить при поиске максимума. Если рейтинг блюда на вершине
кучи не соответствует значению в food_rating, то удаляем его с вершины.
Повторяем процесс, пока не найдем совпадение. При таком подходе в массивах
может скопиться много устаревших значений, но работает быстро.

Лучшее решение:
вариант 1: 236 ms, 51.47 Mb
вариант 2: 83 ms, 50.93 Mb
#hash_table #array #heap
"""
import heapq


class FoodRatings:

    def __init__(
        self,
        foods: list[str],
        cuisines: list[str],
        ratings: list[int],
    ) -> None:
        self.cuisine_food_idx: dict[str, dict[str, int]] = dict()
        self.cuisine_arr: dict[str, list[tuple[int, str]]] = dict()
        self.food_cuisine: dict[str, str] = dict()
        cuisene_len: dict[str, int] = dict()
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_cuisine[food] = cuisine
            if cuisine not in self.cuisine_arr:
                self.cuisine_food_idx[cuisine] = dict()
                self.cuisine_arr[cuisine] = []
                cuisene_len[cuisine] = 0
            idx = cuisene_len[cuisine]
            self.cuisine_food_idx[cuisine][food] = idx
            self.cuisine_arr[cuisine].append((-rating, food))
            cuisene_len[cuisine] = idx + 1
        for k in cuisene_len.keys():
            curr_len = cuisene_len[k]
            arr = self.cuisine_arr[k]
            food_idx = self.cuisine_food_idx[k]
            n = curr_len
            if curr_len & (curr_len - 1):
                n = 1 << curr_len.bit_length()
            new_arr = [(float('inf'),)] * (2 * n - 1)
            for i in range(curr_len):
                idx = n - 1 + i
                new_arr[idx] = arr[i]
                food_idx[arr[i][1]] = idx
            for i in range(n - 2, -1, -1):
                new_arr[i] = min(new_arr[2 * i + 1], new_arr[2 * i + 2])
            self.cuisine_food_idx[k] = food_idx
            self.cuisine_arr[k] = new_arr

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        food_idx = self.cuisine_food_idx[cuisine]
        arr = self.cuisine_arr[cuisine]
        idx = food_idx[food]
        arr[idx] = (-newRating, food)
        prev = (idx - 1) // 2
        while prev >= 0:
            arr[prev] = min(arr[2 * prev + 1], arr[2 * prev + 2])
            prev = (prev - 1) // 2

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_arr[cuisine][0][1]


class FoodRatings2:

    def __init__(
        self,
        foods: list[str],
        cuisines: list[str],
        ratings: list[int],
    ):
        self.cuisine_heap: dict[str, list[tuple[int, str]]] = dict()
        self.food_rating: dict[str, int] = dict()
        self.food_cuisine: dict[str, str] = dict()
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_rating[food] = -rating
            self.food_cuisine[food] = cuisine
            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []
            self.cuisine_heap[cuisine].append((-rating, food))
        for v in self.cuisine_heap.values():
            heapq.heapify(v)

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = -newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        rating, food = heap[0]
        while self.food_rating[food] != rating:
            heapq.heappop(heap)
            rating, food = heap[0]
        return food
