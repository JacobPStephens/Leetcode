# Jacob Stephens - September 15, 2024
# https://leetcode.com/problems/encode-and-decode-strings/description/
# on lintcode for free: https://www.lintcode.com/problem/659/

class Solution:

    def encode(self, strs: List[str]) -> str:
        # if empty, send string longer than any possible code,
        # given constraints, to signal empty list
        if strs == []:
            return "x" * 205

        # encode list elements in the format 
        # element = (len of element + "#" + element) (# is arbitrary delimter)
        for i in range(len(strs)):
            l = len(strs[i])
            strs[i] = str(l) + "#" + strs[i]

        # join together to create string
        s = "".join(strs)

        return s
        
    def decode(self, s: str) -> List[str]:

        # receive empty list signal and return empty list
        if s == "x" * 205:
            return []

        # Initialize variables
        result = []
        readHeader = True
        i = 0

        # Iterate through string
        while i < len(s):
            if (readHeader == True):
                
                # Read the numbers before "#" delimter into an array
                nums = []
                while s[i] != "#":
                    nums.append(int(s[i]))
                    i += 1
                
                # Calculate numerical value given [int, int, ..., int]
                numsToRead = 0
                for j in range(len(nums)):
                    numsToRead += nums[j] * 10**(len(nums)-1-j)

                readHeader = False
            
            else:
                # read numsToRead many characters
                group = s[i+1:i+1+numsToRead]

                # increment i by numsToRead amount
                i = i+1+numsToRead

                # append group to answer
                result.append(group)
                readHeader = True
            
        return result

