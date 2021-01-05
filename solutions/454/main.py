class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        # counts for AB pair sums, CD pair sums, and also res
        res, AB, CD = 0, dict(), dict()

        # get all pairs from AB
        for a in A:
            for b in B:
                AB[a + b] = AB.get(a + b, 0) + 1

        # get all pairs from CD
        for c in C:
            for d in D:
                CD[c + d] = CD.get(c + d, 0) + 1

        # go through pair sums in AB
        for x in AB.keys():
            # check if there is a b such that x + b = 0. or x = -b
            if -x in CD:
                # add the count of these two to res
                res += AB[x] * CD[-x]

        return res