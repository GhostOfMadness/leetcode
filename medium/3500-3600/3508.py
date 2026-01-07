"""
Implement Router.

Реализовать класс Router, поддерживающий следующие операции:
- addPacket: добавить запись, состоящую из 3-х чисел (источник, сервер
  назначения, время отправки) в систему. Если такая запись уже есть в системе,
  то второй раз она не добавляется и функция возвращает False. Если в системе
  закончилось место, то удаляется самая старая запись по времени отправки.
  Записи добавляются в порядке возрастания времени отправки.
- forwardPacket: извлечь из систему самую старую запись и вывести ее.
- getCount: посчитать кол-во записей для заданного сервера назначения,
  поступивших в указанный интервал и еще не извлеченных.

Используем следующие структуры:
- packet_set: множество уникальных записей для текущего времени отправки.
- q: очередь из записей.
- dest_time: словарь пар "сервер назначения - список меток времени отправки".
- dest_idx: словарь пар "сервер назначения - индекс начала актуальных данных".
- dest_size: словарь пар "сервер назначения - кол-во отправок на этот сервер".
- size: размер очереди.
- limit: максимальный размер очереди.
- curr_time: актуальная метка времени.

При добавлении новой записи сначала с помощью packet_set проверяем, что она
уже не добавлена. Если ее метка времени отличается от curr_time, то чистим
множество packet_set и обновляем curr_time.

Если размер очереди уже достиг максимума, то удаляем первый элемент этой
очереди. Если метка времени удаляемой записи совпадает с curr_time, то удаляем
ее и из packet_set (в ином случае ее заведомо там нет, так как packet_set
хранит множество только для самого позднего времени отправки). Также смещаем
индекс начала актуального массива для сервера назначения из удаляемой записи
в dest_time. То есть сам массив будет хранить и старые данные, но актуальный
индекс позволит всегда знать, с какого момента нужно брать данные. Если
в очереди еще есть место, то увеличиваем ее размер на 1. В обоих случаях
добавляем новую запись в packet_set, q, метку времени - в dest_time и
обновляем кол-во отправок для серевера в dest_size.

При извлечении элемента достаем его из начала очереди. Для сервера назначения
сдвигаем индекс начала данных на 1. Если метка времени извлеченного элемента
совпадает с текущей, то удаляем эту запись из packet_set. Также уменьшаем
общий размер очереди на 1.

Чтобы посчитать кол-во отправок для сервера используем бинарный поиск. Сначала
находим индекс первого элемента, который больше или равен startTime, затем -
индекс первого элемента, который строго больше endTime. Разница между ними
и будет ответом. В качестве массива для поиска используем dest_time[dest] от
dest_idx[dest] до dest_size[dest].

Лучшее решение: 433 ms, 79.19 Mb (по времени не оптимально, по памяти - лучше
100% решений)
#queue #hash_table #array
"""
from collections import deque


class Router:

    def __init__(self, memoryLimit: int):
        self.packet_set: set[tuple[int, int, int]] = set()
        self.q: deque[tuple[int, int, int]] = deque([], maxlen=memoryLimit)
        self.dest_time: dict[int, list[int]] = dict()
        self.dest_idx: dict[int, int] = dict()
        self.dest_size: dict[int, int] = dict()
        self.size: int = 0
        self.limit: int = memoryLimit
        self.curr_time: int = None

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_info = (source, destination, timestamp)
        if timestamp == self.curr_time:
            if packet_info in self.packet_set:
                return False
        else:
            self.curr_time = timestamp
            self.packet_set.clear()
        if self.size == self.limit:
            to_remove = self.q.popleft()
            _, dest, timest = to_remove
            if timest == self.curr_time:
                self.packet_set.remove(to_remove)
            self.dest_idx[dest] += 1
        else:
            self.size += 1
        self.packet_set.add(packet_info)
        self.q.append(packet_info)
        if destination not in self.dest_time:
            self.dest_time[destination] = []
            self.dest_idx[destination] = 0
            self.dest_size[destination] = 0
        self.dest_time[destination].append(timestamp)
        self.dest_size[destination] += 1
        return True

    def forwardPacket(self) -> list[int]:
        if not self.q:
            return []
        ans = self.q.popleft()
        _, dest, timest = ans
        self.dest_idx[dest] += 1
        if timest == self.curr_time:
            self.packet_set.remove(ans)
        self.size -= 1
        return list(ans)

    def __bin_seacrh_start(
        self,
        arr: list[int],
        start_idx: int,
        end_idx: int,
        target: int,
    ) -> int:
        left, right = start_idx, end_idx
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return right

    def __bin_seacrh_end(
        self,
        arr: list[int],
        start_idx: int,
        end_idx: int,
        target: int,
    ) -> int:
        left, right = start_idx, end_idx
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_time:
            return 0
        start_idx = self.dest_idx[destination]
        end_idx = self.dest_size[destination]
        arr = self.dest_time[destination]
        start = self.__bin_seacrh_start(arr, start_idx, end_idx, startTime)
        end = self.__bin_seacrh_end(arr, start_idx, end_idx, endTime)
        return end - start
