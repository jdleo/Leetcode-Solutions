class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # result array
        res = []
        # go from left to right
        for i in range(left, right + 1):
            # make sure all digits are divisible by i
            if self.isSelfDividing(i): res.append(i)

        return res

    def isSelfDividing(self, n: int) -> bool:
        i = n

        while i > 0:
            # check if rightmost digit is a 0, or doesnt divide into n
            if i % 10 == 0 or n % (i % 10) != 0: return False
            # get next digit
            i //= 10

        # no problems here
        return True
