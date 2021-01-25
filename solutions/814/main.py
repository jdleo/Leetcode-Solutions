# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root: return None
        # solve left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # return none if leaf AND this val is 0
        if not root.left and not root.right and root.val == 0:
            return None

        return root