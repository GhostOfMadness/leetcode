"""
Process String With Special Operations I.

Дана строка s, состоящая из строчных английских букв и символов *, #, %.
Необходимо получить строку result, которая формируется в результате обработки
s по следующим правилам:
- s[i] == '*' - удалить последний символ result, если он есть, то есть строка
  result непустая.
- s[i] == '#' - продублировать текущий результат и добавить его в конец.
- s[i] == '%' - развернуть текущий результат.
- s[i] = буква - добавить в конец результата.

Используем симуляцию процесса.

Лучшее решение: 38 ms (52.94%), 25.85 Mb (48.34%)
#string #simulation
"""


class Solution:

    def processStr(self, s: str) -> str:
        result = []
        for e in s:
            if e == '*':
                if result:
                    result.pop()
            elif e == '#':
                result.extend(result)
            elif e == '%':
                result = result[::-1]
            else:
                result.append(e)
        return ''.join(result)
