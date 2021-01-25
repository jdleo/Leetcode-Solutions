# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # current sum
    sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        # reverse inorder (start w/ right)
        if root.right: self.convertBST(root.right)

        # add this val to current running sum
        self.sum += root.val
        # set this val to be current running sum
        root.val = self.sum

        # reverse inorder (go left)
        if root.left: self.convertBST(root.left)

        return root