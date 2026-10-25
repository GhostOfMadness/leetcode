"""
Count Days Spent Together.

Даны 4 строки, задающие месяц и день прибытия и отправления Алисы и Боба.
Найти количество дней пересечения этих промежутков. Гарантируется, что все
даты относятся к одному не високосному году.

Переводим строки в формат date модуля datetime и находим разницу в днях между
самой ранней датой отправления и самой поздней датой прибытия. К полученному
числу добавляем 1 для корректного учета всех дней. Если полученная разница
неотрицательная, то даты пересекаются. В ином случае, возвращаем 0.

Лучшее решение: 0 ms (100.00%), 19.14 Mb (93.36%)
#string
"""
import datetime as dt


class Solution:

    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str,
    ) -> int:
        aa = dt.date.fromisoformat(f'2026-{arriveAlice}')
        la = dt.date.fromisoformat(f'2026-{leaveAlice}')
        ab = dt.date.fromisoformat(f'2026-{arriveBob}')
        lb = dt.date.fromisoformat(f'2026-{leaveBob}')
        delta = min(la, lb) - max(aa, ab)
        return max(delta.days + 1, 0)
