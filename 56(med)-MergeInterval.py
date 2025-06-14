# Jacob Stephens - June 14, 2025
# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            headStart, headEnd = intervals[i]
            currentEnd = headEnd
            i += 1
            while i < len(intervals) and currentEnd >= intervals[i][0]:
                currentEnd = max(currentEnd, intervals[i][1])
                i += 1
            res.append([headStart, currentEnd])
        return res
            