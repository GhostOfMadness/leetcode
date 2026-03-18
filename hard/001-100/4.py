"""
Median of Two Sorted Arrays.

Даны два отсортированных массива целых чисел длины m и n. Найти медиану
массива, который получается при объединении исходных с сохранением сортировки.

Ответ можно получить за O(m + n), используя алгоритм объединения массивов из
сортировки слиянием. Но можно поступить иначе. Нам нужно найти медиану, то
есть элемент, стоящий посередине массива, или пару таких элементов в случае
четной длины. Взимное расположение всех остальных элементов значения не имеет,
нужно знать элемент на индексе (m + n) // 2. Сначала проверим, может ли
какой-то элемент из nums1 стоять там. Для этого берем середину nums1 (индекс
mid) и ищем позицию для вставки в nums2 (i). Общая позиция равна mid + i.
Если это значение совпадает с (m + n) // 2, то ответ найден. Если позиция
оказалась левее середины, то сдвигаем левую границу поиска, так как все
элементы до mid тоже не могут быть медианой. Это же верно и для все элементов
до i в nums2, поэтому следующую позицию уже ищем от i, а не от 0. Если mid + i
оказалась правее искомого индекса, то сдвигаем правую границу поиска и ищем
уже в nums2[:i]. Если равенство так и не будет получено, то никакой из
элементов nums1 не является медианой. Поэтому повторяем поиск уже от nums2.

Сама операция бинарного поиска позиции по массиву тоже имеет свою особенность
в случае равенства значений. Можно искать первое значение, которое больше
искомого или больше или равно искомому. Но тогда при двух запусках одинаковые
значения всегда будут оказываться либо в правом, либо в левом краю отрезка
из повторений и медиана не будет найдена. Поэтому будем оринтироваться на
общую позицию относительно искомого индекса (m + n) // 2. Если общая позиция,
то есть сумма индекса элемента в nums1 и текущего варианта вставки в nums2,
больше искомого индекса, то дальше двигаться вправо нет смысла, поэтому
сдвигаем правую границу, если меньше - двигаем левую границу, если равно -
возвращаем текущий mid.

Также нужно учесть случай четной общей длины. Для него нужно знать не только
элемент на (m + n) // 2, но и предыдущий. Так как сортировка сохраняется,
то это либо элемент перед mid в nums1 (при поиске из nums1), либо элемент
перед i из nums2. Выбираем максимум из них и считаем среднее со значением
на mid.

Лучшее решение: 0 ms, 19.66 Mb
#binary_seacrh #array #divide_and_conquer
"""


class Solution:

    def binSeacrh(
        self,
        arr: list[int],
        target: int,
        left: int,
        right: int,
        pos: int,
        targetIdx: int,
    ) -> int:
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                if pos + mid == targetIdx:
                    return mid
                if pos + mid > targetIdx:
                    right = mid
                else:
                    left = mid + 1
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1
        return right

    def searchMedian(
        self,
        searchArr: list[int],
        targetArr: list[int],
        right: int,
        high: int,
    ) -> float | None:
        left = low = 0
        targetIdx, isOdd = divmod(right + high, 2)
        while left < right:
            mid = (left + right) // 2
            i = self.binSeacrh(
                targetArr, searchArr[mid], low, high, mid, targetIdx,
            )
            if mid + i == targetIdx:
                if isOdd:
                    return searchArr[mid]
                else:
                    first = second = float('-inf')
                    if mid > 0:
                        first = searchArr[mid - 1]
                    if i > 0:
                        second = targetArr[i - 1]
                    return (searchArr[mid] + max(first, second)) / 2
            if mid + i < targetIdx:
                left = mid + 1
                low = i
            else:
                right = mid
                high = i

    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> float:
        m = len(nums1)
        n = len(nums2)
        ans = self.searchMedian(nums1, nums2, m, n)
        if ans is not None:
            return ans
        return self.searchMedian(nums2, nums1, n, m)
