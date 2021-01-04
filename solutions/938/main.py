# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # base case
        if not root: return 0

        # check if this val exceeds high (no need to search right subtree)
        if root.val > high: return self.rangeSumBST(root.left, low, high)
        # check if this val exceeds low (no need to search left subtree)
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        # otherwise, return this val + left and right
        return (root.val + self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high))
