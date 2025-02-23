# Jacob Stephens - February 23, 2025
# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def dfs(value, numCoins):
            if (value > amount):
                return
            if (value in dp) and (dp[value] <= numCoins):
                return   
            dp[value] = numCoins
            for coin in coins:
                dfs(value + coin, numCoins + 1)
                
        dfs(0, 0)
        if amount in dp:
            return dp[amount]
        return -1
    