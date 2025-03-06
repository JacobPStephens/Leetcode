# Jacob Stephens - March 5, 2025
# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        hand.sort() # n log(n)
        cardsNeeded = dict()
        i = 0
        lastAdded = float('inf')
        while i < len(hand):

            if hand[i] > lastAdded and len(cardsNeeded) != 0:
                return False

            if hand[i] not in cardsNeeded:
                # add all cards needed to dictionary
                for j in range(hand[i]+1, hand[i]+groupSize):
                    if j not in cardsNeeded:
                        cardsNeeded[j] = 0
                    cardsNeeded[j] += 1
                    lastAdded = j
                    #print(cardsNeeded)
                    
            else:
                cardsNeeded[hand[i]] -= 1
                if cardsNeeded[hand[i]] == 0:
                    del cardsNeeded[hand[i]]
            i += 1
        return len(cardsNeeded) == 0
