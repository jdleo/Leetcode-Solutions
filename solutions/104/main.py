# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive solution
    def maxDepth(self, root: TreeNode) -> int:
        # base case
        if not root: return 0
        # this root is valid so its +1 depth with whatever the max of both subtrees is
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative solution
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        # stack for DFS (add tuple of node val, and depth)
        stack = [(root, 1)]
        # max depth
        res = 1

        # go until stack empty
        while stack:
            # pop top
            cur, depth = stack.pop()
            # set new max depth
            res = max(res, depth)
            # add left and right if not null
            if cur.left: stack.append((cur.left, depth + 1))
            if cur.right: stack.append((cur.right, depth + 1))

        return res