# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # generate inorder path
        path = self.inorder(root)

        # build recursively
        return self.build(root, path, 0, len(path) - 1)

    # helper method to recursively build balanced, sorted tree
    def build(self, root, nums, left, right):
        # base case
        if left > right: return None

        # get midpoint, and set new root
        mid = (left + right) >> 1
        root = TreeNode(nums[mid])

        # use properties of BST to build left and right
        root.left = self.build(root, nums, left, mid - 1)
        root.right = self.build(root, nums, mid + 1, right)

        return root

    # helper method for providing an iterative, inorder path of tree
    def inorder(self, root: TreeNode) -> list[int]:
        # stack and path for our inorder traversal
        stack, path = [], []

        # go while stack or root
        while root or stack:
            if root:
                # keep going left
                stack.append(root)
                root = root.left
            else:
                # pop from stack
                root = stack.pop()
                # add to path (visit)
                path.append(root.val)
                # go right now
                root = root.right

        return path
