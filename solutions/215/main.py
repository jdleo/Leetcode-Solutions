from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        heap = []

        # go through nums
        for num in nums:
            # push to min heap
            heappush(heap, num)

            # if over capacity, pop (bounds problem to o(nlogk) instead of o(nlogn))
            if len(heap) > k:
                heappop(heap)

        # result is at top of heap
        return heap[0]