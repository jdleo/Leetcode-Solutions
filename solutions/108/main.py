# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # recursively build tree
        return self.builder(nums, 0, len(nums) - 1)

    def builder(self, nums, left, right):
        # base case
        if left > right: return None

        # calculate mid point (BST logic)
        mid = (left + right) >> 1

        # this root is num at mid
        root = TreeNode(nums[mid])

        # set left and right subtrees with standard BST logic
        root.left = self.builder(nums, left, mid - 1)
        root.right = self.builder(nums, mid + 1, right)

        return root