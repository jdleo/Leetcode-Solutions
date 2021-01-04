class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # if you see this, i couldnt resist the python golf ;) forgive me
        return [[i ^ 1 for i in row[::-1]] for row in A]
