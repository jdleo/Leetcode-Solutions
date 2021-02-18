class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        # number of students doing homework at time queryTime
        res = 0

        # go thru start times and endtimes
        for start, end in zip(startTime, endTime):
            # check if querytime lies in this interval
            if start <= queryTime <= end:
                res += 1

        return res