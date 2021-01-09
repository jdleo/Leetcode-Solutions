class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # result (total subarrays) and current running sum
        res = curSum = 0
        # dictionary for storing prefix sums (0:1) cuz we have 1 occurrence of sum 0
        pre = {0: 1}

        # iterate thru nums
        for num in nums:
            # add to running sum
            curSum += num

            # check if sum - k in prefix sums
            if curSum - k in pre:
                # add how many there are
                res += pre[curSum - k]

            # increment subarray count for sum
            pre[curSum] = pre.get(curSum, 0) + 1

        return res