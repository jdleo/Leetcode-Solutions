class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # running product, and sum
        p, s = 1, 0

        # reduce n to 0
        while n > 0:
            # get rightmost digit
            rightmost = n % 10
            # add rightmost product/sum
            p *= rightmost
            s += rightmost
            # move to next digit
            n //= 10

        # subtract sum from product
        return p - s