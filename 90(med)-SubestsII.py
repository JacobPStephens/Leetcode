# Jacob Stephens - February 8, 2025
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(subset, i):

            if i == len(nums):
                res.append(subset.copy())
                return 

            current_choice = nums[i]

            # include current number
            subset.append(current_choice)
            dfs(subset, i+1)

            # don't include current number (skips all of that number)
            while (i < len(nums)) and (nums[i] == current_choice):
                i += 1

            subset.pop()
            dfs(subset, i)
    
        nums.sort()
        res = []
        dfs([], 0)
        
        return res
