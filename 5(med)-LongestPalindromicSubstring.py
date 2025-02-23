# Jacob Stephens - February 23, 2025
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        
        def getMaxPalindrome(l, r):
            count = -1 if l == r else 0
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                count += 2
                l -= 1
                r += 1
            return count

        maxLength = 0
        for i in range(len(s)):
            count = max(getMaxPalindrome(i, i), getMaxPalindrome(i, i+1))
            if count > maxLength:
                maxLength = count
                l, r = (i - (maxLength // 2) + (1 - count % 2), i + maxLength // 2)
    
        print(maxLength, l, r)
        return s[l:r+1]
