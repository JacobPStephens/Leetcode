# Jacob Stephens - February 14, 2025
# https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bounded(r, c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))

        freshFruitCount = 0
        # queue of rotten fruit where rotten fruit = (row, col, minute rotten)
        queue = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruitCount += 1
                elif grid[i][j] == 2:
                    queue.appendleft((i, j, 0))
        
        # bfs 
        mostRecentSpoil = 0
        while queue:
            r, c, minute = queue.pop()
            mostRecentSpoil = max(mostRecentSpoil, minute)

            for delta_r, delta_c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                new_r = r + delta_r
                new_c = c + delta_c

                if not bounded(new_r, new_c):
                    continue
                
                if grid[new_r][new_c] == 0 or grid[new_r][new_c] == 2:
                    continue
                
                # turn fresh fruit rotten
                grid[new_r][new_c] = 2
                queue.appendleft((new_r, new_c, minute + 1))
                freshFruitCount -= 1


        if freshFruitCount:
            return -1
        return mostRecentSpoil
