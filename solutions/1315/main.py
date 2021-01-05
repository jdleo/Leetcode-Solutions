# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self,
                           root: TreeNode,
                           parent: TreeNode = None,
                           grandparent: TreeNode = None) -> int:
        # base case
        if not root: return 0

        # only take this value if grandparent is even valued
        res = root.val if grandparent and grandparent.val % 2 == 0 else 0

        # add sums from left and right subtrees
        # but make parent grandparent, and cur node parent
        res += self.sumEvenGrandparent(root.left, root, parent)
        res += self.sumEvenGrandparent(root.right, root, parent)

        return res