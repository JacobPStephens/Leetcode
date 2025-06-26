# Jacob Stephens - June 26, 2025
# https://leetcode.com/problems/swim-in-rising-water/

from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def bounded(r: int, c: int) -> bool:
            return (0 <= r < len(grid) and 0 <= c < len(grid))

        n = len(grid)
        lowestWater = []
        for _ in range(n):
            lowestWater.append([float('inf')] * n)
        lowestWater[0][0] = grid[0][0]   

        queue = collections.deque([(0, 0, grid[0][0])])
        while queue:
            r, c, level = queue.pop()
            for delta_r, delta_c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                new_r = r + delta_r
                new_c = c + delta_c
                if not bounded(new_r, new_c):
                    continue
                
                if level < lowestWater[new_r][new_c]:
                    neighborLevel = grid[new_r][new_c]
                    queue.append((new_r, new_c, max(level, neighborLevel)))
                    lowestWater[new_r][new_c] = max(level, neighborLevel)
        
        return lowestWater[n-1][n-1]

