"""
Partition Array According to Given Pivot.

Дан массив целых чисел nums и целое число pivot, которое точно есть в этом
массиве. Необходимо вернуть массив, в котором сначала идут все числа меньшие
pivot, затем - равные ему, потом - больше него. Относительный порядок чисел
должен быть сохранен при перестройке.

Создадим 2 дополнительных массива, в которые будет сохранять числа меньше
(less) и больше (greater) pivot, а также заведем счетчик equal_cnt для подсчета
значений, равных pivot. В качестве ответа вернем объединение массивов less,
массива равных pivot значений, который формируется на основе их количества,
а также массива greater.

Лучшее решение: 27 ms (73.61%), 33.66 Mb (77.63%)
#array #simulation
"""


class Solution:

    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less, greater = [], []
        equal_cnt = 0
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal_cnt += 1
            else:
                greater.append(num)
        return [*less, *[pivot] * equal_cnt, *greater]
