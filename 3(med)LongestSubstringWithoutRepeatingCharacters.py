# Jacob Stephens - October 2, 2024
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = dict()
        maxLength = 0

        i = 0
        while i < len(s):
            
            if s[i] not in visited:
                visited[s[i]] = i
                i += 1

            else:
                maxLength = max(maxLength, len(visited))
                i = visited[s[i]] + 1
                visited.clear()

        maxLength = max(maxLength, len(visited))

        return maxLength
        
