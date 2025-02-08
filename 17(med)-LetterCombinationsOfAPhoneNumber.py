# Jacob Stephens - February 8, 2025
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        digitMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }   
        
        def backtrack(combination, i):

            if len(combination) == len(digits):
                print("Possible combination", combination)
                res.append(combination)
                return

            curr_digit = digits[i]

            for letter in digitMap[curr_digit]:
                combination += letter
                backtrack(combination, i + 1)
                combination = combination[:-1]

        res = []
        backtrack("", 0)
        return res
