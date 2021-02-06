class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # biggest possible box number is box #45 (ball #99999)
        boxes = [0] * 46

        # go from low limit to high limit inclusive
        for i in range(lowLimit, highLimit + 1):
            # put this ball in its respective box
            boxes[self.sumOfDigits(i)] += 1

        # return the box with the most balls
        return max(boxes)

    # helper method to calculate sum of digits
    def sumOfDigits(self, num: int) -> int:
        res = 0

        while num > 0:
            res += (num % 10)
            num //= 10

        return res
