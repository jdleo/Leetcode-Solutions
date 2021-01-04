class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # recursively generate parantheses
        self.generate(res, '', n, n)

        return res

    # helper method to generate parentheses
    def generate(self, res, cur, left, right):
        # check if we used all left and right parentheses
        if left == 0 and right == 0:
            # add cur to res
            res.append(cur)
        else:
            # check if we have left pars left
            if left > 0:
                self.generate(res, cur + '(', left - 1, right)

            # check if we can use a matching right par
            if right > left:
                self.generate(res, cur + ')', left, right - 1)