from collections import deque


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        # result array
        res = []
        # build initial permutation (and use deque for appendleft)
        P = deque([i for i in range(1, m + 1)])
        # go thru queries
        for query in queries:
            # find position of this query
            index = P.index(query)
            # add position to res
            res.append(index)
            # remove at this index
            P.remove(query)
            # insert at beginning
            P.appendleft(query)

        return res
