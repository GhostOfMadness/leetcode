"""
Find the Lexicographically Largest String From the Box I.

Необходимо найти лексикографически наибольшую подстроку, которую можно получить
после разбиения word на numFriends непустых частей.

Лучшее решение: 28 ms, 18.08 Mb
"""


class Solution:

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_length = n - numFriends + 1
        ans = word[:max_length]
        for left in range(1, n):
            coml = min(n - left, max_length)
            if word[left: left + coml] > ans[:coml]:
                ans = word[left: left + coml]
        return ans
