class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # last index each char is seen at
        last = {char: i for i, char in enumerate(S)}

        # left, right pointers and result array
        left, right, res = 0, 0, []

        # go through S
        for i, char in enumerate(S):
            # update right to be rightmost index
            right = max(right, last[char])

            # check if i caught up to right
            if i == right:
                # this is a partition, add length of partition
                res.append(right - left + 1)
                # update left (start index for next partition)
                left = right + 1

        return res