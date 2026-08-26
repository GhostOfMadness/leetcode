"""
Concatenate Non-Zero Digits and Multiply by Sum II.

Дана строка s, состоящая из цифр, а также массив queries, где queries[i] =
[l, r], левая и правая границы отрезка (обе границы включены в интервал).
Числом x для отрезка [l, r] называется конкатенация всех ненулевых цифр
на этом интервале с сохранением исходного порядка, а число sum - сумма всех
цифр в x. Для каждого запроса в queries необходимо найти значение x * sum
по модулю 10 ** 9 + 7.

Используем префиксные массивы nums, digitSums и numLens:
- nums[i] - модуль числа, полученный конкатенацией цифр на s[:i].
- digitSums[i] - сумма цифр числа x на s[:i].
- numLens[i] - длина числа x на s[:i].

Сумма цифр числа x на отрезке [l, r] равна digitSums[r + 1] - digitSums[l].
Само число x считается как nums[r + 1] - nums[l] * 10 ** numLen, где numLen -
длина числа x. Чтобы каждый раз не высчитывать 10 в большой степени создадим
массив xdegree, в котором будем хранить модули десяток во всех степенях от
нулевой до максимальной длины числа. Для ответа умножаем найденное число
на сумму цифр в нем и берем модуль.

Лучшее решение: 467 ms (67.86%), 56.36 Mb (52.38%)
#prefix_sum #math #string
"""


class Solution:

    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        mod = 10 ** 9 + 7

        n = len(s)
        nums = [0] * (n + 1)
        digitSums = [0] * (n + 1)
        numLens = [0] * (n + 1)
        for i in range(n):
            digit = int(s[i])
            digitSums[i + 1] = digitSums[i] + digit
            if digit:
                nums[i + 1] = ((nums[i] * 10) % mod + digit) % mod
                numLens[i + 1] = numLens[i] + 1
            else:
                nums[i + 1] = nums[i]
                numLens[i + 1] = numLens[i]
        
        maxNumLen = numLens[n]
        xdegree = [1] * (maxNumLen + 1)
        for i in range(1, maxNumLen + 1):
            xdegree[i] = (xdegree[i - 1] * 10) % mod

        qLen = len(queries)
        ans = [0] * qLen
        for i in range(qLen):
            l, r = queries[i]
            digitSum = digitSums[r + 1] - digitSums[l]
            numLen = numLens[r + 1] - numLens[l]
            num = (nums[r + 1] - (nums[l] * xdegree[numLen]) % mod) % mod
            ans[i] = (num * digitSum) % mod
        return ans
