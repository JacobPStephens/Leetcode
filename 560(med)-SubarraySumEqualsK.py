# Jacob Stephens - March 24, 2025
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # generate prefix sum
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
 
        # use prefix sum to find subarrays
        d = { k: 1 }

        res = 0
        for num in prefixSum:
            if num in d:
                res += d[num]
            if (num+k) not in d:
                d[num+k] = 0
            d[num+k] += 1
        
        return res
