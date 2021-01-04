class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # minimum total time
        res = 0

        # go through points
        for i in range(1, len(points)):
            # get last x, y, and cur x, y
            lastX, lastY = points[i - 1]
            curX, curY = points[i]

            # minimum distance is max between delta x and delta y
            res += max(abs(curY - lastY), abs(curX - lastX))

        return res