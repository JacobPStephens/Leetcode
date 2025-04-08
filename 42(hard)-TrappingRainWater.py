# Jacob Stephens - April 8, 2025
# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        def identifyWallPairs(height):
            walls = []
            l = 0
            r = len(height) - 1
            leftMax = (0, height[0])
            rightMax = (r, height[r])

            while l <= r:
                if leftMax[1] <= height[l]:
                    if (l - leftMax[0] > 1):
                        walls.append([leftMax, (l, height[l])])
                    leftMax = (l, height[l])

                if rightMax[1] <= height[r]: 
                    if (rightMax[0] - r > 1):
                        walls.append([(r, height[r]), rightMax])
                    rightMax = (r, height[r])
                if leftMax[1] <= rightMax[1]:
                    l += 1
                else:
                    r -= 1
            return walls

        def getWaterArea(wallPair, height):
            
            leftWall = wallPair[0]
            rightWall = wallPair[1]

            water = 0
            waterCeiling = min(leftWall[1], rightWall[1])
            for i in range(leftWall[0]+1, rightWall[0]):
                water += waterCeiling - height[i]

            return water

        wallPairs = identifyWallPairs(height)
        totalWater = 0
        for wallPair in wallPairs:
            totalWater += getWaterArea(wallPair, height)

        return totalWater
    