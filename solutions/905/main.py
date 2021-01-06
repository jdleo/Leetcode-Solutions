class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # left and right pointers
        left, right = 0, len(A) - 1

        # go until pointers meet
        while left < right:
            # check if left is in correct place
            if A[left] % 2 == 0:
                left += 1
                continue

            # check if right is in correct place
            if A[right] % 2:
                right -= 1
                continue

            # swap and increment both
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

        # sorted in-place
        return A