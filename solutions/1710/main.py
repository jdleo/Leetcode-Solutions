class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        res = 0

        # first sort box types by number of units per box (greedy) DESCENDING
        boxTypes.sort(key=lambda x: -x[1])

        # go through box types
        for boxes, units in boxTypes:
            # get minimum between number of boxes, and capacity we have left
            boxesTaken = min(boxes, truckSize)
            # multiply boxes taken by units
            res += boxesTaken * units
            # subtract boxes taken from truckSize
            truckSize -= boxesTaken
            # early stop
            if truckSize == 0: break

        return res
