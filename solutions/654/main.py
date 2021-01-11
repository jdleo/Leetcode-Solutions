# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        # call our helper with left and right as initial nums size
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: list[int], left: int, right: int) -> TreeNode:
        # base case
        if left > right: return None

        # get index of max
        maxIdx = left
        for i in range(left + 1, right + 1):
            if nums[i] > nums[maxIdx]: maxIdx = i

        # current value is number at max
        root = TreeNode(nums[maxIdx])

        # build left subtree (left of maxIdx) right subtree (right of maxIdx)
        root.left = self.build(nums, left, maxIdx - 1)
        root.right = self.build(nums, maxIdx + 1, right)

        return root