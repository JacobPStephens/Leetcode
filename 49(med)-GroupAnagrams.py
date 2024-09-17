# Jacob Stephens - September 13, 2024
# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):

        # init dict with default value to empty list
        d = defaultdict(list)

        # iterate through each string
        for s in strs:

            # create array of len 26 where
            # where i=0 -> a, i=1 -> b, ..., i=25 -> z
            chCount = [0] * 26
            for c in s:
                chCount[ord(c) - ord('a')] += 1

            # key is unique counts of characters (as tuple)
            # value is string that contains that set of characters
            d[tuple(chCount)].append(s)

        # result is list of [lists of anagram strings]
        result = []
        for key in d:
            result.append(d[key])
        
        return result
