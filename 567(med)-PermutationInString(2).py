# Jacob Stephens - January 19, 2025
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        # generate reference dict
        ref = [0] * 26
        for i in range(len(s1)):
            ref[ord(s1[i]) - 97] += 1
            ref[ord(s2[i]) - 97] -= 1

        i = 0
        j = len(s1)
        while j < len(s2):
            
            if ref == [0] * 26:
                print(f"Found at {(i, j)=}")
                return True

            ref[ord(s2[i]) - 97] += 1
            ref[ord(s2[j]) - 97] -= 1

            i += 1
            j += 1
        
        if ref == [0] * 26:
            return True
        return False
