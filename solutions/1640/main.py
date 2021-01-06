class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # result array from building pieces together
        res = []
        # store each piece along with their starting piece in hash map
        starts = {piece[0]: piece for piece in pieces}

        # go through array and build out res
        for num in arr:
            # add piece to res
            res.extend(starts.get(num, []))

        # arr should be == res if this was true
        return res == arr
