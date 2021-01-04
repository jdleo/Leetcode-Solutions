# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # levels
        levels = []

        # helper function to do dfs traversal, tracking depth
        def dfs(root: TreeNode, depth=0):
            # base case
            if not root: return

            # check if theres a level created for this depth yet
            if len(levels) == depth: levels.append([])
            # and add this node val to this depth in levels
            levels[depth].append(root.val)
            # go left and right
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        # start DFS
        dfs(root)

        return levels