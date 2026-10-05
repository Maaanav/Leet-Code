class Solution:
    def checkValidString(self, s: str) -> bool:
        min_op = max_op = 0

        for char in s:
            if char == '(':
                min_op += 1
                max_op += 1
            elif char == ')':
                min_op -= 1
                max_op -= 1
            else:
                min_op -= 1
                max_op += 1

            if max_op < 0:
                return False

            min_op = max(0, min_op)

        return min_op == 0  
