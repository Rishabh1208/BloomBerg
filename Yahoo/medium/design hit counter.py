import collections


class HitCounter(object):

    def __init__(self):
        self.deque = collections.deque()

    def hit(self, timestamp):
        self.deque.append(timestamp)

    def getHits(self, timestamp):
        while self.deque and timestamp - self.deque[0] >= 300:
            self.deque.popleft()
        return len(self.deque)

# Binary Search

class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left, right = 0, len(self.hits) - 1
        target = timestamp - 300

        while left <= right:
            mid = (left + right) // 2

            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return len(self.hits) - left
