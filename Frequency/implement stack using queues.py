# approach 1 --> Two queues push - O(1) pop - O(N)

from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0

# using single queue push --> O(N) and pop --> O(1)
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        q_len = len(self.q)
        while q_len > 1:
            self.q.append(self.q.popleft())
            q_len -= 1

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
