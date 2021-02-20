# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root: return res
        self.helper(res, root)
        return res

    def helper(self, res, root):
        res.append(root.val)
        for child in root.children:
            self.helper(res, child)        