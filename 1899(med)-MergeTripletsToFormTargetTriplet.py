# Jacob Stephens - March 6, 2025
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = [False] * 3
        for triplet in triplets:
            targetIndeces = self.checkValidity(triplet, target)
            if not targetIndeces:
                continue
            for index in targetIndeces:
                res[index] = True
        #print(res)
        return all(res)    

    def checkValidity(self, triplet, target):

        targetIndeces = []
        for i in range(3):
            # determine if has target
            if triplet[i] == target[i]:
                targetIndeces.append(i)
            
            if triplet[i] > target[i]:
                return False

        return targetIndeces
