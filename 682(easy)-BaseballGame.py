# Jacob Stephens - March 24, 2025
# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = 0
        stack = []
        for op in operations:
            if op == "C":
                removed = stack.pop()
                res -= removed
            else:
                if op == "+":
                    newScore = stack[-1] + stack[-2]
                elif op == "D":
                    newScore = stack[-1] * 2
                else:
                    newScore = int(op)
                stack.append(newScore)
                res += newScore

        return res
