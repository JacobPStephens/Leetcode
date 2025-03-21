# Jacob Stephens - March 20, 2025
# https://leetcode.com/problems/minimum-size-subarray-sum/description

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0
        l = r = 0
        res = 0

        while r < len(nums):
            total += nums[r]      
            while total >= target:
                res = r - l + 1
                total -= nums[l]
                l += 1

            r += 1
            if l != 0 and l < len(nums):
                total -= nums[l]
                l += 1

        return res
        