# Jacob Stephens - March 30, 2025
# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        k = min(k, len(nums)-1)
        currentSet = set()
        for i in range(k+1):
            if nums[i] in currentSet:
                return True
            currentSet.add(nums[i])

        i = 0
        j = k + 1

        while j < len(nums):
            currentSet.remove(nums[i])
            if nums[j] in currentSet:
                return True
            currentSet.add(nums[j])
            i += 1
            j += 1

        return False


        # O(n^2) solution
        # k = min(k, len(nums)-1)

        # def isUnique(window):
        #     return len(window) == len(set(window))


        # for i in range(len(nums) - k):
        #     if not isUnique(nums[i:i+k+1]):
        #         return True

        # return False