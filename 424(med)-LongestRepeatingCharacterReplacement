# Jacob Stephens - January 19, 2025

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxCount = 0
        ans = 0
        i = 0
        j = 0
        while j < len(s):
            l = j - i + 1
            # add new character from right
            counts[s[j]] += 1

            # update max character count
            if counts[s[j]] > maxCount:
                maxCount = counts[s[j]]

            # check validity of window
            if maxCount >= -k + l:
                ans = max(ans, l)

            # remove from left if invalid window
            else:
                counts[s[i]] -= 1
                i += 1

            j += 1
        
        return ans
