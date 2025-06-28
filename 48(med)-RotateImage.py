# Jacob Stephens - June 28, 2025
# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def rotateRing(k: int, origin: int) -> None:
            # k is length of this side
            for i in range(k-1):
                tmp1 = matrix[0+origin][0+origin+i] 

                # top-left with bot-left
                matrix[0+origin][0+origin+i] = matrix[k+origin-1-i][0+origin]
                # bot-left with bot-right
                matrix[k+origin-1-i][0+origin] = matrix[k+origin-1][k+origin-1-i]
                # bot-right with top-right
                matrix[k+origin-1][k+origin-1-i] = matrix[0+origin+i][k+origin-1]
                # top-right with top-left
                matrix[0+origin+i][k+origin-1] = tmp1
        
        n = len(matrix)
        origin = 0
        for i in range(n, 0, -2):
            rotateRing(i, origin)
            origin += 1
   