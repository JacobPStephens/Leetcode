# Jacob Stephens - January 26, 2025
# https://leetcode.com/problems/lru-cache/description/

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.queue = deque([])

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.queue.remove(key)
        self.queue.appendleft(key)

        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.queue.remove(key)

        self.queue.appendleft(key)
        self.d[key] = value

        if len(self.queue) > self.capacity:
            del self.d[self.queue.pop()]
        