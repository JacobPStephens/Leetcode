# Jacob Stephens - September 17, 2024
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:

        # initialize stack and loop through string
        stack = []
        for ch in s:

            # append to opens to stack
            if ch == "(":
                stack.append("p")

            elif ch == "[":
                stack.append("b")

            elif ch == "{":
                stack.append("c")

            # pop from stack if conditions are met, otherwise return flase
            elif ch == ")":
                if (not stack) or (stack[-1] != "p"):
                    return False
                stack.pop()

            elif ch == "]":
                if (not stack) or (stack[-1] != "b"):
                    return False
                stack.pop()

            elif ch == "}":
                if (not stack) or (stack[-1] != "c"):
                    return False
                stack.pop()
        
        # false if stack is not len zero
        if stack:
            return False

        return True
