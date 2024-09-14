class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        
        chCount = [0] * 26

        for i in range(len(s)):
            chCount[ord(s[i]) - ord('a')] += 1
            chCount[ord(t[i]) - ord('a')] -= 1
        
        print(chCount)
        for num in chCount:
            if num != 0:
                return False

        return True
