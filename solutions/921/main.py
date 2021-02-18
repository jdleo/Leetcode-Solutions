class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # stack to hold parantheses, and result (adds)
        stack, res = [], 0

        # go thru string
        for char in S:
            # check if closing parentheses
            if char == ')':
                # check matching parantheses in stack
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    # we need to add
                    res += 1
            else:
                # just add to stack
                stack.append("(")

        # res + whatever is left in stack (needs matching)
        return res + len(stack)