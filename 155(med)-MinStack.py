# Jacob Stephens - March 10, 2024
# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_value:
            self.min_value = val
            self.min_stack.append(val)
        
    def pop(self) -> None:
        top_value = self.stack.pop()
        if top_value == self.min_stack[-1]:
            self.min_stack.pop()
            if self.min_stack:
                self.min_value = self.min_stack[-1]
            else:
                self.min_value = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
