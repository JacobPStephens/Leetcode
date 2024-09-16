# Jacob Stephens - September 16, 2024
# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # This solution is O(n) despite how it initially appears
        # Linear because hash map does cancels iteration of redundant numbers

        #nums = [8, 3, 2, 5, 4, 6, 1, 1]
        visited = {num: False for num in nums}
        numsSet = set(nums)

        # Initialize max sequence length to 0
        maxCount = 0

        # Iterate through numbers in set
        for num in numsSet:

            # Don't iterate if already visited 
            # (already part of another, explored, sequence)
            if visited[num] == True:
                print(f"skip {num}")
                continue
            
            # initialize count of this sequence
            count = 1

            # check all numbers in sequence below num
            i = 1
            while num-i in numsSet:
                print(f"Found {num-i}")
                print(f"Making {num-i} true")
                visited[num-i] = True
                i += 1
                count += 1
                print(f"count: {count}")
                
            # check all numbers in sequence above num
            i = 1
            while num+i in numsSet:
                print(f"Found {num+i}")
                print(f"Making {num+i} true")
                visited[num+i] = True
                i += 1
                count += 1
                print(f"count: {count}")
            
            # update largest sequence length
            if count > maxCount:
                maxCount = count
                print(f"New max count: {maxCount}")
            

        return maxCount
