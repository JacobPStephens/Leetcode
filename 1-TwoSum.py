# Jacob Stephens - September 13, 2024
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()
        # iterate through nums once O(n)
        for i in range(len(nums)):
            # diff is the number needed to sum to target
            diff = target - nums[i]
            # found solution
            if diff in d:
                return [d[diff], i]
            # otherwise add value and its index
            else:
                d[nums[i]] = i
