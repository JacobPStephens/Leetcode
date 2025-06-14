# Jacob Stephens - February 17, 2025
# http://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bounded(r, c):
            return (0 <= r < len(heights) and 0 <= c < len(heights[0]))

        # traverse through ocean and return everything visited
        def exploreSea(stack, visited):
            while stack:
                r, c, height = stack.pop()
                for delta_r, delta_c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    new_r = r + delta_r
                    new_c = c + delta_c
                    
                    if not bounded(new_r, new_c):
                        continue
                    adjHeight = heights[new_r][new_c]   
                
                    if (new_r, new_c, adjHeight) in visited:
                        continue
                    if height <= adjHeight:
                        stack.add((new_r, new_c, adjHeight))
                        visited.add((new_r, new_c, adjHeight))
            return visited

        # generate starting pacific and atlantic sets where pacific 
        # is  top and left and atlantic is right and bottom
        pcfc, atlc = set(), set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i == 0) or (j == 0):
                    pcfc.add((i, j, heights[i][j]))
                if (i == len(heights) - 1) or (j == len(heights[0]) - 1):
                    atlc.add((i, j, heights[i][j]))

        # return intersection of pacific visited and atlantic visited
        res = []
        for pair in exploreSea(pcfc, pcfc.copy()).intersection(exploreSea(atlc, atlc.copy())):
            res.append([pair[0], pair[1]])
        return res
        