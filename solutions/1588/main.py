class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # total sum
        res = 0

        # iterate thru all odd numbers up to length of arr
        for i in range(1, len(arr) + 1, 2):
            # iterate through all possible slices
            for j in range(0, len(arr) - i + 1):
                # add sum of this slice to res
                res += sum(arr[j:j + i])

        return res