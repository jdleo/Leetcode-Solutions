# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive solution
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root: return None

        # get reference to left and right subtrees
        left, right = root.left, root.right

        # invert
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root

    # iterative solution
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root: return None

        # stack for DFS
        stack = [root]

        while stack:
            # get current by popping
            cur = stack.pop()

            # swap left and right
            cur.left, cur.right = cur.right, cur.left

            # add children
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)

        return root