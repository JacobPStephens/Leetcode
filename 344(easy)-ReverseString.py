# Jacob Stephens - March 20, 2025
# https://leetcode.com/problems/reverse-string/description/


class Solution:
    def reverseString(self, s: List[str]) -> None:

        l = 0
        r = len(s) - 1

        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp

            l += 1
            r -= 1
        
        return s