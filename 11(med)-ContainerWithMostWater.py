# Jacob Stephens - October 11, 2024
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1

        maxArea = 0
        while l < r:

            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(area, maxArea)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

       
