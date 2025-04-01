# Jacob Stephens - April 1, 2025
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        sol = []
        for a in asteroids: 
            if a > 0:
                stack.append(a)
            else:
                while stack and abs(a) > stack[-1]:
                    stack.pop()
                if not stack:
                    sol.append(a)
                elif abs(a) == stack[-1]:
                    stack.pop()

        sol.extend(stack)
        return sol