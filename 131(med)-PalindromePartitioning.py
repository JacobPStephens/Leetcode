# Jacob Stephens - February 9, 2025
# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def part(current, i, j):
            if i >= len(current) or j >= len(current[i]) - 1:
                if isPalindrome(current[-1]):
                    res.append(current.copy())
                return

            beforeSplit = current[i]

            # split and call function
            rightSplit = current[i][j+1:]
            current[i] = current[i][:j+1]
            current.append(rightSplit)

            if isPalindrome(current[i]):
                part(current, i + 1, 0)

            # undo split and call function
            current.pop()
            current[i] = beforeSplit
            part(current, i, j + 1)
        

        def isPalindrome(s):
            i = 0
            while i < (len(s) // 2):
                if s[i] != s[-(i+1)]:
                    return False
                i += 1
            return True

        res = []
        part([s], 0, 0)
        return res
            