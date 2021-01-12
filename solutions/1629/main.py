class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        # current slowest key, and duration
        slowest = (0, releaseTimes[0])

        # go through rest of releaseTimes
        for i in range(1, len(releaseTimes)):
            # set new slowest release time
            slowest = max(slowest, (i, releaseTimes[i] - releaseTimes[i - 1]),
                          key=lambda x: (x[1], keysPressed[x[0]]))

        # return character of slowest
        return keysPressed[slowest[0]]