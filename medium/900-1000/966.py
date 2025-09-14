"""
Vowel Spellchecker.

Дан список слов wordlist и список запросов queries. Для каждого запроса
проводится проверка по следующим правилам:
- если слово есть в wordlist (с учетом регистра), то оно заносится в ответ.
- если слово совпадает со словом в wordlist без учета регистра (например,
  query = "kiTe",  word = "KITE), то в ответ заносится первое вхождение
  формы этого слова в wordlist.
- если слово совпадает со словом в wordlist путем замены гласных в слове
  и без учета регистра (query = "Cube", word = "cAbU"), то в ответ заносится
  первое вхождение формы этого слова в wordlist.
Вывести список ответов для всех запросов.

Сначала заведем множество words, в котором хранятся исходные версии слов с
учетом регистра, и словарь d. Ключами словаря d будут схемы слов, в которых
все гласные заменены на пробелы. Каждой такой схеме соответствует массив
из 2-х элементов. На 0-м индексе стоит слово, соответствующее первому
вхождению этой схемы в wordlist. На 1-м индексе стоит словарь, в котором
для каждого уникального набора гласных для такой схемы указана первое
вхождение такого слова. Схема и наборы гласных хранятся в нижнем регистре.
d = {scheme: [first_scheme_match, {vowels: first_vowels_match, ...}], ...}

Проходимся по массиву queries. Если слово есть в множестве words, то заносим
его в ответ и переходим к следующему. В ином случае, получаем схему и набор
гласных для этого слова в нижнем регистре. Если такой схемы нет в словаре d,
то такого слова вообще нет в списке, поэтому в ответ добавляем пустую строку.
Если схема есть, но не такого же набора гласных, то добавляем первое вхождение
схемы в wordlist. Если есть и схема, и набор гласных, то добавляем первое
вхождение формы этого слова в wordlist (к этому моменту уже проверили, что
самого исходного слова в списке нет).

Лучшее решение: 27 ms, 21.99 Mb
#hash_table #array #string
"""


class Solution:

    def __get_vowels_scheme(self, word: str) -> tuple[str, str]:
        vowels, scheme = '', ''
        for e in word:
            if e in 'aeiou':
                vowels += e
                scheme += ' '
            else:
                scheme += e
        return (vowels, scheme)

    def spellchecker(
        self,
        wordlist: list[str],
        queries: list[str],
    ) -> list[str]:
        words = set(wordlist)
        d = dict()
        for word in wordlist:
            lower_form = word.lower()
            vowels, scheme = self.__get_vowels_scheme(lower_form)
            if scheme not in d:
                d[scheme] = [word, {vowels: word}]
            elif vowels not in d[scheme][1]:
                d[scheme][1][vowels] = word
        n = len(queries)
        ans = [None] * n
        for i in range(n):
            query = queries[i]
            if query in words:
                ans[i] = query
                continue
            lower_form = query.lower()
            vowels, scheme = self.__get_vowels_scheme(lower_form)
            if scheme not in d:
                ans[i] = ''
            elif vowels not in d[scheme][1]:
                ans[i] = d[scheme][0]
            else:
                ans[i] = d[scheme][1][vowels]
        return ans
