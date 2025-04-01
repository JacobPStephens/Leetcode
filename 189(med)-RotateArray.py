# Jacob Stephens - April 4, 2025
# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) time; O(n) space 
        i = 0 
        j = (len(nums) - k) % len(nums)
        clone = nums.copy()
        while i < len(nums):
            nums[i] = clone[j]
            i += 1
            j = (j + 1) % len(nums)

        return nums