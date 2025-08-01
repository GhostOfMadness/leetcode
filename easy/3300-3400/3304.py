"""
Find the K-th Character in String Game I.

Исходная слово содержит букву 'a'. На каждом шаге к слову добавляется оно
само, сдвинутое на 1 вправо по алфавиту (a -> ab -> abbc -> abbcbccd).
Необходимо найти k-й символ. В битовом представлении нужно посчитать кол-во
нулевых бит до первого единичного бита справа и кол-во единичных бит.

Лучшее решение: 0 ms, 17.70 Mb
"""


class Solution:

    def naive_solution(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            word += ''.join(chr(ord(e) + 1) for e in word)
        return word[k - 1]

    def str_solution(self, k: int) -> str:
        bits = bin(k)[2:]
        steps = (
            sum(1 for bit in bits if bit == '1')
            + len(bits)
            - bits.rfind('1')
            - 1
        )
        return chr(ord('a') + steps - 1)

    def bit_solution(self, k: int) -> str:
        k = k - 1
        cnt = 97
        while k:
            cnt += k & 1
            k = k >> 1
        return chr(cnt)
