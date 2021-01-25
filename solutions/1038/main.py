# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # reversed inorder traversal
        if root.right: self.bstToGst(root.right)

        self.val += root.val
        # modify root's value to be current + val
        root.val = self.val

        if root.left: self.bstToGst(root.left)
        return root