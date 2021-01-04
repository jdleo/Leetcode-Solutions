# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # stack for inorder
        stack = []

        # while there is something in stack or root
        while root or stack:
            if root:
                # add to stack and keep going left
                stack.append(root)
                root = root.left
            else:
                # no more left subtrees, pop from stack
                root = stack.pop()
                # this is where wed normally print inorder val
                # but we can decrement k and see if its 0 (this would be k'th smallest)
                k -= 1
                if k == 0: return root.val
                # go right now
                root = root.right

        # none found
        return -1