class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # current max altitude (biker starts at altitude 0)
        mx = curSum = 0

        # go thru gains
        for g in gain:
            # update running sum, and set new max height
            curSum += g
            mx = max(mx, curSum)

        return mx
        