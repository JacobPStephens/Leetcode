# Jacob Stephens - June 15, 2025
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        i = 1
        
        while i < len(intervals):
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                res += 1
            else:
                prevEnd = intervals[i][1]

            i += 1
        return res
