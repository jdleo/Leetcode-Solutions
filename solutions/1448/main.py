# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, mx=float('-inf')) -> int:
        # base case
        if not root: return 0

        # compare current value with current max in path
        if root.val >= mx:
            # add 1 (good node) + sum of good nodes in left and right
            # also change new max to this node
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(
                root.right, root.val)
        else:
            # this is bad node, but keep looking for good nodes
            return self.goodNodes(root.left, mx) + self.goodNodes(
                root.right, mx)
