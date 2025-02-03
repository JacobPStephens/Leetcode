# Jacob Stephens - January 25, 2025
# https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            #print(nums)

            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            
            nums[abs(nums[i])] *= -1

            i += 1
