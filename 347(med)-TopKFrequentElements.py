# Jacob Stephens - February 14, 2025
# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # build count dictionary
        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # create heap from counts
        maxHeap = [(-item[1], item[0]) for item in count.items()]
        heapq.heapify(maxHeap)

        # pop k elements from heap
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1]) 
        return res

