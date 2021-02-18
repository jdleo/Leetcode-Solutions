# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode, cur: int = 0) -> int:
        # base case
        if not root: return 0

        # left shift current number, add current bit to it
        cur = (cur << 1) + root.val

        # check if this is leaf node
        if not root.left and not root.right:
            # return cur
            return cur

        # return result of left + right subtrees
        return self.sumRootToLeaf(root.left, cur) + self.sumRootToLeaf(root.right, cur)