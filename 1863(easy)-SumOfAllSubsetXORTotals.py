# Jacob Stephens - March 31, 2025
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def XORTotal(subset):
            total = 0
            for num in subset:
                total = total ^ num
            return total

        def generateSubsets(current, i):

            if i == len(nums):
                return XORTotal(current)
                
            current.append(nums[i])
            add = generateSubsets(current, i + 1)

            current.pop()
            skip = generateSubsets(current, i + 1)
            return add + skip

        return generateSubsets([], 0)
