from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        # initialize max heap, min heap
        self.maxHeap, self.minHeap = [], []
        # initialize median for now
        self.median = 0

    def addNum(self, num: int) -> None:
        # figure out which heap to put num in
        if not self.maxHeap or num < -self.maxHeap[0]:
            # this belongs in max heap
            heappush(self.maxHeap, -num)
        else:
            # this belongs in min heap
            heappush(self.minHeap, num)

        # rebalance min heap
        self.rebalance()

        # set new median which is the bigger heap's root, or avg of both
        if len(self.maxHeap) == len(self.minHeap):
            # avg of both roots
            self.median = (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            # its the one in max heap
            self.median = -self.maxHeap[0]
        else:
            # its the one in min heap
            self.median = self.minHeap[0]

    def findMedian(self) -> float:
        # simply return median
        return self.median

    # helper method to rebalance heaps
    def rebalance(self):
        # check if even needs rebalancing
        if len(self.maxHeap) - len(self.minHeap) > 1:
            # need to put one of max heap into min heap
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            # need to put one of min heap into max heap
            heappush(self.maxHeap, -heappop(self.minHeap))