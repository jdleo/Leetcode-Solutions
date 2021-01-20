# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # base case
        if not root: return None
        # check if val is less than root, then search left
        if val < root.val: return self.searchBST(root.left, val)
        # check if val is greater than root, then search right
        if val > root.val: return self.searchBST(root.right, val)
        # this means this val == root. this is the one
        return root