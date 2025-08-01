"""
Daily Temperatures.

Для каждого значения температуры в массиве найти количество дней до
ближайшего более теплого дня справа.

Будем хранить в стеке индексы элементов. Каждый новый элемент выталкивает
из стека все индексы, для которых температура меньше текущей. Ответом
для таких индексов будет разница между текущей позицией и удаленной.

Лучшее решение: 83 ms, 27.02 Mb
"""


class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [0]
        for i in range(1, n):
            e = temperatures[i]
            while stack and e > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
