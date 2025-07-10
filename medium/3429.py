"""
Reshedule Meetings for Maximum Free Time I.

Необходимо сдвинуть k встреч, не изменяя из порядок, чтобы получить наибольший
по длине интервал свободного времени.

Проходим окном размера k по событиям и считаем общую длину интервалов до,
после и внутри окна. Выбираем наибольший вариант.

Лучшее решение: 44 ms, 36.26 mb
"""


class Solution:
    def maxFreeTime(
        self,
        eventTime: int,
        k: int,
        startTime: list[int],
        endTime: list[int],
    ) -> int:
        n = len(endTime)
        startTime.append(eventTime)
        endTime.append(0)
        curr = sum(startTime[i] - endTime[i - 1] for i in range(1, k + 1))
        print(curr)
        ans = curr
        for j in range(1, n - k + 1):
            curr = (
                curr
                - (startTime[j - 1] - endTime[j - 2])
                + (startTime[j + k] - endTime[j + k - 1])
            )
            ans = max(ans, curr)
        return ans
