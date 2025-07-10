"""
Reschedule Meetings for Maximum Free Time II.

Даны массивы времени начала и окончания встреч в рамках события, которое
длится от 0 до eventTime. Встречи не пересекаются между собой. Необходимо
перенести максимум одну встречу таким образом, чтобы получить наибольший по
длительности интервал непрерывного свободного времени. Порядок встреч может
поменяться, но они не должны пересекаться.

Каждую встречу можно сдвинуть к одному из соседей, тогда интервал свободного
времени будет равен сумме интервалов до и после встречи, то есть
startTime[i] - endTime[i - 1] + startTime[i + 1] - endTime[i]. Так как
разрешено менять порядок встреч, то текущую встречу можно перенести на любое
свободное время, подходящее по длительности. То есть нужно знать размер
наибольшего интервала слева и справа от встречи. Максимум слева можно
обновлять при проходе по циклу, так как на каждой итерации слева будет
добавляться 1 новый интервал. Для максимума справа создадим массив max_arr,
в котором и насчитаем нужные значения. Так как текущий интервал не должен
учитываться, то интервал справа от события 0 опускается.

Лучшее решение: 237 ms, 38.71 Mb
"""


class Solution:

    def maxFreeTime(
        self,
        eventTime: int,
        startTime: list[int],
        endTime: list[int],
    ) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)
        max_arr = [0] * n
        for i in range(n - 1, 0, -1):
            max_arr[i - 1] = max(max_arr[i], startTime[i + 1] - endTime[i])
        j = 0
        max_left = 0
        ans = 0
        for i in range(n):
            before = startTime[i] - endTime[i - 1]
            after = startTime[i + 1] - endTime[i]
            curr = before + after
            length = endTime[i] - startTime[i]
            max_right = max_arr[j]
            if max(max_left, max_right) >= length:
                curr += length
            ans = max(ans, curr)
            j += 1
            max_left = max(max_left, before)
        return ans


if __name__ == '__main__':
    res = Solution()
    eventTime = 5
    startTime = [1]
    endTime = [2]
    print(res.maxFreeTime(eventTime, startTime, endTime))
