# Jacob Stephens - March 3, 2025
# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netGas = [gas[i] - cost[i] for i in range(len(gas))]
        netGas = netGas + netGas[:-1]
        maxFound = -float('inf')
        maxIdx= -1
        total = 0
        i = j = 0
        while j < len(netGas):
            total += netGas[j]
            if total < 0:
                i = j + 1
                total = 0
            if total > maxFound:
                maxFound = total
                maxIdx = i
            j += 1

        if sum(netGas[:len(gas)]) < 0:
            return -1
        return maxIdx
