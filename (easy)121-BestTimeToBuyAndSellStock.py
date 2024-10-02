# Jacob Stephens - October 2, 2024
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minStock = 10001
        maxMoney = 0

        for i in range(len(prices)):

            if prices[i] < minStock:
               minStock = prices[i]
               continue
            
            maxMoney = max(maxMoney, prices[i] - minStock)
                
        return maxMoney
