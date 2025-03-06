# Jacob Stephens - March 6, 2025
# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        end = 0
        largest = 0
        while largest < len(nums) - 1:
            start = end
            end = largest + 1
            for i in range(start, end):
                if (i + nums[i]) > largest:
                    largest = (i + nums[i])
            jumps += 1

        return jumps