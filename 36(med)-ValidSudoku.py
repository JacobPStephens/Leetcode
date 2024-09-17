# Jacob Stephens - September 15, 2024
# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        #board = [["1","2",".",".","3",".","1",".","2"],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
        box = []

        for j in range(9):
            row = []
            
            for i in range(9):
                
                #print(board[j][i])
                if board[j][i] != ".":
                    row.append(board[j][i])

                # Handle boxes every 3rd col
                if (j % 3 == 0):
                    
                    for k in [0, 1, 2]:
                        if board[i][j+k] != ".":
                            box.append(board[i][j+k])

                    if (i % 3 == 2):
                        #print(box)
                        if len(box) != len(set(box)):
                            print("Dupl in box: ", box)
                            return False
                        box = []

            # check for duplicate in row
            if len(row) != len(set(row)):
                print("Dupl in row: ", row) 
                return False

        # check each column
        for i in range(9):
            col = []
            for j in range(9):
                
                if board[j][i] != ".":
                    col.append(board[j][i])
            
            if len(col) != len(set(col)):
                print("Dupl in col: ", col)
                return False

        return True
