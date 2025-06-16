# Jacob Stephens - June 16, 2025
# https://leetcode.com/problems/target-sum/description/

from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(len(nums)):
            for t, count in dp.copy().items():
                dp[t] -= count
                if dp[t] == 0:
                    del dp[t]
                dp[t + nums[i]] += count
                dp[t - nums[i]] += count
            #print(dp)
        return dp[target]
    