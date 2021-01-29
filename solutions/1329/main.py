from heapq import heappush, heappop


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        # get dimensions
        m, n = len(mat), len(mat[0])

        # collection of min heaps (key is diagonal buckets)
        buckets = dict()

        # go thru matrix
        for row in range(m):
            for col in range(n):
                # check if this diagonal key hasnt been created yet
                if row - col not in buckets: buckets[row - col] = []

                # push this value in matrix to corresponding minheap
                heappush(buckets[row - col], mat[row][col])

        # go back thru matrix again
        for row in range(m):
            for col in range(n):
                # this value should be the smallest in current diagonal heap
                # since it's sorted ascending
                mat[row][col] = heappop(buckets[row - col])

        return mat