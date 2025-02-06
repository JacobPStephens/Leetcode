# Jacob Stephens - February 5, 2025
# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(current, remaining):

            #print(f'{current=} {remaining=}')
            
            if not remaining:
                res.append(current.copy())
                   
            i = 0
            while i < len(remaining):
                dfs(current + [remaining[i]], remaining[:i] + remaining[i+1:])

                i += 1

        dfs([], nums)

        return res
