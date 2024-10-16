class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        permChars = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord('a')
            permChars[idx] += 1
        
        #print("start ", permChars)

        i = 0
        j = i + len(s1)

        while j < len(s2) + 1:
            splice = s2[i:j]
            hasPerm = self.checkPermutation(splice, permChars)
            
            if hasPerm:
                return True

            i += 1
            j += 1

        return False

    def checkPermutation(self, splice, permChars):
        permCharsCopy = permChars.copy()
        for ch in splice:
            idx = ord(ch) - ord('a')
            permCharsCopy[idx] -= 1
        
        #print(splice, permCharsCopy)
        if permCharsCopy == [0] * 26:
            return True
        return False
