# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # stack for inorder, and inorder path
        stack, path = [], []

        # keep going while there is a root, or stuff in stack
        while root or stack:
            if root:
                # add to stack keep going left
                stack.append(root)
                root = root.left
            else:
                # pop from stack
                root = stack.pop()
                # add to path (visit inorder)
                path.append(root.val)
                # go right now
                root = root.right

        return path