# Jacob Stephens - April 3, 2025
# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:

        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        dp = [0] * (n + 1)
        for num in range(1, n+1):
            numSquares = float('inf')
            for square in squares:
                if num - square >= 0:
                    numSquares = min(numSquares, dp[num - square] + 1)
            dp[num] = numSquares

        return dp[n]

       