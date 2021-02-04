from collections import deque


class RecentCounter:
    def __init__(self):
        # initialize queue for pings
        self.pings = deque()

    def ping(self, t: int) -> int:
        # add this ping
        self.pings.append(t)
        # shave off all the pings in queue that are not within 3000 ms
        while self.pings[0] < t - 3000:
            self.pings.popleft()

        # everything left in queue is within 3000 ms, guaranteed
        return len(self.pings)