# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: return None
        # stack for dfs
        stack = [(original, cloned)]
        # until stack is empty
        while stack:
            # pop cur
            curOriginal, curCloned = stack.pop()

            # check if this is target
            if curOriginal == target:
                # return same node in cloned tree
                return curCloned
            
            # add left and right subtrees (if non null)
            if curOriginal.left: stack.append((curOriginal.left, curCloned.left))
            if curOriginal.right: stack.append((curOriginal.right, curCloned.right))
            

        # never found one
        return None