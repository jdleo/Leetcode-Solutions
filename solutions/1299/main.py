class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # current greatest element
        maxx = -1

        # go through array backwards
        for i in reversed(range(len(arr))):
            # set this current number to max (greatest from right)
            # and set new max (if need be)
            arr[i], maxx = maxx, max(maxx, arr[i])

        return arr