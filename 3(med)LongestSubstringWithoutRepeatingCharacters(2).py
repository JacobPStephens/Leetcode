# Jacob Stephens - January 25, 2025
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        l = 0
        r = 1

        visited = set(s[l])
        maxLength = 1
        currentLength = 1

        while r < len(s):

            if s[r] not in visited:
                visited.add(s[r])
                currentLength += l
                maxLength = max(maxLength, currentLength)
            
            else:
                repeatedCharacter = s[r]
                while s[l] != repeatedCharacter:
                    visited.remove(s[l])
                    currentLength -= 1
                    l += 1
                
                l += 1
            r += 1

        return maxLength
