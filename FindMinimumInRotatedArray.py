class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:# or (nums[0] < nums[-1]):
            return nums[0]
        
        l = 0
        r = len(nums)-1
        m = (r+l) // 2

        while True:
            m = (r+l) // 2
            if nums[m] < nums[m-1]:
                return nums[m]
            
            if nums[m] > nums[m+1]:
                return nums[m+1]
            
            elif nums[m] < nums[l]:
                r = m - 1
            elif nums[m] > nums[l]:
                l = m + 1
