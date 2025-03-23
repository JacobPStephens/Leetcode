# Jacob Stephens - March 22, 2025
# https://leetcode.com/problems/find-k-closest-elements/description/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = 0
        r = k

        while r < len(arr) and (abs(x - arr[r]) < abs(x - arr[l]) or arr[r] < x):
            l += 1
            r += 1

        return arr[l:r]