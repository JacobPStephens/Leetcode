''' Given a string, find the length of the longest substring
in it with no more than K distinct characters '''

# problem link: https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.-pattern-sliding-window/1.3-longest-substring-with-k-distinct-characters-medium.md

class Solution:
    def solve(self, s: str, k: int) -> int:

        l = r = 0
        counts = dict()
        while r < len(s):
            if s[r] not in counts:
                counts[s[r]] = 0
            counts[s[r]] += 1

            if len(counts) > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1
            r += 1
        return r-l
