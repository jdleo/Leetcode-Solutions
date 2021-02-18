class Solution:
    def sumZero(self, n: int) -> list[int]:
        # result array 
        res = []

        # check if odd
        if n & 1:
            # set first number to be 0 and reduce n to be even
            res.append(0)
            n -= 1

        # go until no more numbers
        while n > 0:
            # add negative and positive n
            res.append(-n)
            res.append(n)
            # jump 2
            n -= 2


        return res