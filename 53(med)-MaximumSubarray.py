# Jacob Stephens - February 28, 2025
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = -float('inf')
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            largest = max(largest, currentSum)
            if currentSum < 0:
                currentSum = 0

        return largest