# Jacob Stephens - February 13, 2025
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0
        visited = set()

        def bounded(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        # depth first search
        def exploreIsland(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                for delta_r, delta_c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    new_r = r + delta_r
                    new_c = c + delta_c

                    if not bounded(new_r, new_c):
                        continue
                    
                    # discard water (0's) and already visited islands
                    if grid[new_r][new_c] == "0" or (new_r, new_c) in visited:
                        continue

                    stack.append((new_r, new_c))
                visited.add((r, c))

        # scan through every point
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == "0" or (row, col) in visited:
                    continue

                # every unexplored 1 is a new island
                exploreIsland(row, col)
                numIslands += 1

        return numIslands
