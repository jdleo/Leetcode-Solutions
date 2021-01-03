class Solution:
    def numberOfSteps (self, num: int) -> int:
        # if num is 0, its just 0
        if not num: return 0
        # number of steps
        steps = 0

        # reduce to 0
        while num > 0:
            # if last bit is 1, it requires subtraction AND division, if 0, it only required division
            steps += 2 if num & 1 else 1
            # right shift (divide by 2)
            num >>= 1

        # do steps - 1 because last bit did not require 2 steps
        return steps - 1