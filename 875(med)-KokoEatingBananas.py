# Jacob Stephens - October 18, 2024
# https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # key (int) = banana eating rate; 
        # value (bool) = is possible or not to eat all bananas at rate k under given hours
        explored = {}

        # establish min and max k to be used as bounds for binary search
        max_k = max(piles)
        min_k = 1
    
        # we know, by problem definition, it's possible with max k
        explored[max_k] = True

        # loop until we find minimum k
        # (guaranteed to find minimum k)
        while True:
            
            # determine mid point k and calculate hours required with that rate k
            mid = (min_k + max_k) // 2
            hoursReq = self.calcTimeToEat(piles, mid)
            #print(f"Mid of next iteration: {mid}")

            # we ate too slow, so binary search up and increase rate
            if hoursReq > h:
                explored[mid] = False

                # check stop condition
                # if this k is false, but k+1 is true, k+1 must be minimum possible
                if explored.get(mid+1, False):
                    #print(f"Solution found: {mid+1}")
                    return (mid+1)

                min_k = mid
            
            # we ate quickly, so binary search down to optimize with slower rate
            else:
                explored[mid] = True

                # if we are exploring 1, it is the answer
                if mid == 1:
                    print("Solution is 1")
                    return 1
                
                max_k = mid
    
    # given piles and k, return the hours required to eat all bananas
    def calcTimeToEat(self, piles, k):

        hoursReq = 0
        for pile in piles:
            hoursReq += math.ceil(pile / k)
        
        return hoursReq
