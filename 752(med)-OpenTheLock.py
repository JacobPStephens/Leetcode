# Jacob Stephens - March 27, 2025
# https://leetcode.com/problems/open-the-lock/

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # Assumptions:
        # first encounter of a combo is the minimum number of turns

        # converts combo of type [int] to string
        def convertComboToString(combo):
            return "".join([str(x) for x in combo])

        # cast to set for O(1) lookup
        deadends = set(deadends)

        # edge cases
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        
        # Design of queue:
        # queue = [pairs], pair = (combo, turns (int)), combo = [int]
        queue = collections.deque([([0, 0, 0, 0], 0)])
        visited = {"0000"}
        while queue:
            currentCombo, turns = queue.pop()
            for i in range(4):
                for direction in [-1, 1]:
                    nextCombo = currentCombo.copy()
                    
                    if direction == -1 and nextCombo[i] == 0:
                        nextCombo[i] = 9
                    elif direction == 1 and nextCombo[i] == 9:
                        nextCombo[i] = 0
                    else:
                        nextCombo[i] = nextCombo[i] + direction

                    strRep = convertComboToString(nextCombo)
                    if strRep == target:
                        return turns + 1
                    
                    if strRep not in deadends and strRep not in visited:
                        queue.appendleft((nextCombo, turns + 1))
                        visited.add(strRep)
                        
        return -1
