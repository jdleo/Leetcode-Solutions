class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # result array
        res = []

        # go from 0 to n
        for i in range(n):
            # add number in first half, number in second half
            res.append(nums[i])
            res.append(nums[i + n])

        return res