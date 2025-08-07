"""
2106. Maximum Fruits Harvested After at Most K Steps.

Дан массив fruits, состоящий из пар "позиция - количество фруктов", исходная
позиция на числовой прямой startPos и максимальное число шагов k. За один шаг
можно пройти 1 единицу по числовой прямой в любую сторону. Найти максимальное
количество фруктов, которое можно собрать, двигаясь от исходной позиции, не
более чем за k шагов.

Смена направления движения имеет смысл только 1 раз, в ином случае какие-то
из расстояний будут дублироваться, что сократит общую дистанцию, которую
можно пройти. То есть от исходной позиции можно пойти сначала налево, затем
вернуться и пойти направо, или наоборот.

Используем метод 2-х указателей. left установим на последнюю позицию, которую
можно достичь, если двигаться только влево, right - первый элемент с позицей
больше или равной, чем исходная. Оба значения можно найти бинарным поиском.
Будем двигать левый указатель, пока остаемся левее исходной позиции. Также
при сдвиге будем уменьшать левую сумму leftsum, то есть сумму фруктов,
которые можно собрать слева от исходной позиции. Внутри итеарции будем
накапливать правую сумму rightsum.

dist - расстояние от исходной позиции до текущей. У нас 2 варианта движения,
нужно выбрать оптимальный. Если мы движемся сначало влево, потом направо,
то направо сможем уйти на k - 2 * dist, если наоборот, то (k - dist) // 2.
Необходимо покрыть как можно большее расстояние, поэтому выбираем максимум
из этих значений и заносим в to_right. Сдвигаем right к startPos + to_right
и наращиваем правую сумму. Обновляем ответ на сумму leftsum и rightsum,
если она больше текущего значения. Сдвигаем left на 1 и уменьшаем leftsum
на выброшенное значение.

Лучшее решение: 82 ms, 52.46 Mb
"""


class Solution:

    def __bin_search(self, fruits: list[list[int]], target: int):
        left = 0
        right = len(fruits)
        mid = (left + right) // 2
        while left < right:
            if fruits[mid][0] == target:
                return mid
            if fruits[mid][0] > target:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        return mid

    def maxTotalFruits3(
        self,
        fruits: list[list[int]],
        startPos: int,
        k: int,
    ) -> int:
        n = len(fruits)
        left = self.__bin_search(fruits=fruits, target=startPos - k)
        right = self.__bin_search(fruits=fruits, target=startPos)
        leftsum = sum([e[1] for e in fruits[left: right]])
        rightsum = 0
        ans = 0
        while left < n and fruits[left][0] < startPos:
            dist = startPos - fruits[left][0]
            to_right = max(k - 2 * dist, (k - dist) // 2)
            while right < n and fruits[right][0] <= startPos + to_right:
                rightsum += fruits[right][1]
                right += 1
            ans = max(ans, leftsum + rightsum)
            leftsum -= fruits[left][1]
            left += 1
        while right < n and fruits[right][0] <= startPos + k:
            rightsum += fruits[right][1]
            right += 1
        return max(ans, rightsum)
