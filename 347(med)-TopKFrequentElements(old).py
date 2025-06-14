# Jacob Stephens - September 13, 2024
# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create default dict with values of 0
        d = defaultdict(int)

        # increment frequency by 1 each time number appears in list
        for num in nums:
            d[num] += 1

        # alist types = [(freq, num), (freq, num)]
        alist = []
        for num in d:
            alist.append((d[num], num))

        # sort to put most frequent elements first
        alist.sort(reverse=True)

        # print the first k indeces
        result = []
        for i in range(k):
            result.append(alist[i][1])

        return result
        
