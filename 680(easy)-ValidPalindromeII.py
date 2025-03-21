# Jacob Stephens - March 21, 2025
# https://leetcode.com/problems/valid-palindrome-ii/description/

# fun solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # palindrome check
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return (False, l, r)
                l += 1
                r -= 1
            return (True, -1, -1)

        p, l, r = isPalindrome(0, len(s) - 1)
        if p:
            return True

        return isPalindrome(l + 1, r)[0] or isPalindrome(l, r - 1)[0]
