# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        # seen for individual uncontaminated nodes
        self.seen = set()
        # build seen set with dfs
        self.dfs(root)

    # helper method for dfs traversal
    def dfs(self, root: TreeNode, x: int = 0):
        if root:
            # add current x to set
            self.seen.add(x)
            # go left and right
            # left = 2 * x + 1, right = 2 * x + 2
            self.dfs(root.left, 2 * x + 1)
            self.dfs(root.right, 2 * x + 2)

    def find(self, target: int) -> bool:
        # simply check set
        return target in self.seen