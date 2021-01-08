# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative solution
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        # current max depth, and current sum and that depth
        maxDepth = curSum = 0
        # stack for dfs
        stack = [(root, 0)]
        # while stack isnt empty
        while stack:
            # get current node
            root, depth = stack.pop()

            # check if depth is same as max depth
            if depth == maxDepth:
                # add to sum
                curSum += root.val
            elif depth > maxDepth:
                # that means its bigger
                maxDepth, curSum = depth, root.val

            # go left, right
            if root.left: stack.append((root.left, depth + 1))
            if root.right: stack.append((root.right, depth + 1))

        return curSum

    # recursive solution
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # current max depth, and current sum and that depth
        maxDepth = curSum = 0

        # dfs helper function
        def dfs(root: TreeNode, depth=0):
            nonlocal maxDepth, curSum
            # base case
            if not root: return

            # check if depth is same as max depth
            if depth == maxDepth:
                # add to sum
                curSum += root.val
            elif depth > maxDepth:
                # that means its bigger
                maxDepth, curSum = depth, root.val

            # go left, right
            dfs(root.left, depth + 1), dfs(root.right, depth + 1)

        dfs(root)
        return curSum