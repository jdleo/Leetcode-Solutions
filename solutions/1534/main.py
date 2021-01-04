class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # number of good triplets
        res = 0

        # iterate through all triplets, but ensure i < j < k
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    # three conditions that must be satisfied
                    cond1 = abs(arr[i] - arr[j]) <= a
                    cond2 = abs(arr[j] - arr[k]) <= b
                    cond3 = abs(arr[i] - arr[k]) <= c

                    # good triplet if all 3 conds satisfy
                    if cond1 and cond2 and cond3: res += 1

        return res