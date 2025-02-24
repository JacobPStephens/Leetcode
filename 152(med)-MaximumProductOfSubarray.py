# Jacob Stephens - February 24, 2025
# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        # split problem by zeros into 'subproblems'
        parts = []
        part = []
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                part.append(nums[i])
                i += 1
            parts.append(part.copy())
            part = []
            i += 1

        # helper function to calculate product of list
        def product(numberList):
            if not numberList:
                return 0
            p = 1
            for num in numberList:
                p *= num
            return p

        # solve each subproblem 
        def productOfSub(subproblem):
            if len(nums) == 1:
                return subproblem[0]

            negatives = [i for i in range(len(subproblem)) if subproblem[i] < 0]
            if len(negatives) % 2 == 0:
                return product(subproblem)

            excludingFirst = product(subproblem[negatives[0]+1:])
            excludingLast = product(subproblem[:negatives[-1]])

            return max(excludingFirst, excludingLast)

        # solve each subproblem, updated product accordingly
        maxProduct = -float('inf')
        for subproblem in parts:
            res = productOfSub(subproblem)
            maxProduct = max(maxProduct, res)
        
        return maxProduct
