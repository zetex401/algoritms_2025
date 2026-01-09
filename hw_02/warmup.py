def reverse_string(s: str) -> str:
    stack = []
    for ch in s:
        stack.append(ch)

    result = []
    while stack:
        result.append(stack.pop())

    return "".join(result)


class QueueFromStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        # Если stack_out пуст, перекладываем из stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("dequeue from empty queue")

        return self.stack_out.pop()


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string("Алматы"))

    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    q.enqueue(4)
    print(q.dequeue())  # 3
    print(q.dequeue())  # 4
