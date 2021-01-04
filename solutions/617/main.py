# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive solution
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # base case
        if not t1 and not t2: return None

        # get values from t1 and t2 (0 if one of them is null)
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0

        # new merged node is them summed
        node = TreeNode(v1 + v2)

        # set left and right subtrees recursively
        node.left = self.mergeTrees(t1.left if t1 else None,
                                    t2.left if t2 else None)

        node.right = self.mergeTrees(t1.right if t1 else None,
                                     t2.right if t2 else None)

        return node