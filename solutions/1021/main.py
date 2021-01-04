class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # result char array
        res = []
        # current paranthese balance
        bal = 0

        # iter thru string
        for char in S:
            # check if this is opening and not outer
            if char == '(' and bal > 0: res.append(char)
            elif char == ')' and bal > 1: res.append(char)

            # adjust balance based on par
            bal += 1 if char == '(' else -1

        # join res to string
        return ''.join(res)