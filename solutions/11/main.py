class Solution:
    def maxArea(self, height: List[int]) -> int:
        # result (most water)
        res = 0
        # pointers for left and right columns
        left, right = 0, len(height) - 1

        # go until pointers meet
        while left < right:
            # calculate water trapped between these two columns
            area = (right - left) * min(height[left], height[right])

            # set new max area
            res = max(res, area)

            # move forward the lower container
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res