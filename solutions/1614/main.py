class Solution:
    def maxDepth(self, s: str) -> int:
        # current depth, and max depth
        curD = maxD = 0

        # iterate thru string
        for char in s:
            # increment depth if opening par, decrement if closing
            if char == '(':
                curD += 1
                # set new max
                maxD = max(maxD, curD)
            elif char == ')':
                curD -= 1

        return maxD