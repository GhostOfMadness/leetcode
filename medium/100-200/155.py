"""
Min Stack.

Реализовать класс MinStack, в котором доступны все операции со стеком, а также
реализована операция минимума на стеке за константное время.

Создадим отдельный массив prefix, где будем хранить минимум на префиксе. При
добавлении значения в стек новое значение prefix будет равно минимуму из
prefix[-1] и val. При удалении элемента из стека просто удаляем последнее
значение из prefix.

Лучшее решение: 4 ms, 21.32 Mb
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix.append(min(self.prefix[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]

    def __str__(self):
        return ', '.join(map(str, self.stack))


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
