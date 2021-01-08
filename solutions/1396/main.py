from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        # to store checkins
        self.checkins = dict()
        # to store trips (default to empty tuple, representing total time and trip count)
        self.trips = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # store this checkin under id w/ start station and time
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # get corresponding checkin
        startStation, startTime = self.checkins[id]
        # delete reference to save mem
        del self.checkins[id]
        # encode trip key
        key = (startStation, stationName)
        # get current total time and trip count
        totalTime, count = self.trips[key]
        # set new
        self.trips[key] = (totalTime + (t - startTime), count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # calculate simple average time / count
        totalTime, count = self.trips[((startStation, endStation))]
        return totalTime / count