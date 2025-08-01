"""
Candy.

N детей стоят в одну линию. Необходимо определить наименьшее кол-во конфет,
которое необходимо раздать, чтобы каждый ребенок получил минимум одну конфету,
а дети с более высоким рейтингом получили больше конфет, чем их соседи.

Лучшее решение: 7 ms, 19.83 Mb
"""


import json
import random
import time


class Solution:

    def candy(self, ratings: list[int]) -> int:
        acc = 1
        i = 1
        n = len(ratings)
        prev = 1
        while i < n:
            if ratings[i] > ratings[i - 1]:
                prev += 1
                acc += prev
                i += 1
            elif ratings[i] == ratings[i - 1]:
                prev = 1
                acc += prev
                i += 1
            else:
                seq = 0
                while i < n and ratings[i] < ratings[i - 1]:
                    prev -= 1
                    acc += prev
                    i += 1
                    seq += 1
                acc += (1 - prev) * (seq + int(1 >= prev))
                prev = 1
        return acc

    def candy2(self, ratings: list[int]) -> int:
        acc = 1
        prev = 1
        seq = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if seq:
                    acc += (1 - prev) * (seq + int(1 >= prev))
                    seq = 0
                    prev = 1
                prev = 1 + int(ratings[i] > ratings[i - 1]) * prev
                acc += prev
            else:
                seq += 1
                prev -= 1
                acc += prev
        acc += (1 - prev) * (seq + int(1 >= prev))
        return acc

    def test(self, file_name: str) -> None:
        data = json.load(open(file_name))
        total = len(data)
        acc = 0
        for test_data in data:
            input_data = test_data['test']
            ans = test_data['answer']
            func_ans = self.candy2(ratings=input_data)
            if ans != func_ans:
                print(f'Массив: {" ".join(map(str, input_data))}')
                print(f'Ответ функции: {func_ans}')
                print(f'Правильный ответ: {ans}')
            else:
                acc += 1
        print(f'Успешно пройдено {acc} из {total} тестов')

    def timed(self, f, *params) -> float:
        start = time.perf_counter()
        f(*params)
        end = time.perf_counter()
        return end - start

    def time_test(self, size: int, n_iter: int = 10):
        acc1 = acc2 = 0
        for _ in range(n_iter):
            ratings = random.choices(range(2 * 10 ** 4 + 1), k=size)
            acc1 += self.timed(self.candy, ratings)
            acc2 += self.timed(self.candy2, ratings)
        print(f'Время работы функции `candy` = {acc1:.5f} сек')
        print(f'Время работы функции `candy2` = {acc2:.5f} сек')
