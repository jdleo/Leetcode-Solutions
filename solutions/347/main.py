from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts for each number
        counts = defaultdict(int)

        # count each number's frequency
        for num in nums:
            counts[num] += 1

        # min heap
        heap = []

        # go through each num, freq in counts
        for num, freq in counts.items():
            # push to min heap
            heappush(heap, (freq, num))

            # check if min heap exceeded capacity (bounds this problem to o(nlogk))
            if len(heap) > k:
                heappop(heap)

        # result array
        res = []

        # keep popping from heap
        while heap:
            res.append(heappop(heap)[1])

        return res