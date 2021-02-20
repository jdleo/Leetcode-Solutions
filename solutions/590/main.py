# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        res = []
        if not root: return res
        self.helper(res, root)
        return res

    def helper(self, res: list[int], root: 'Node'):
        for child in root.children:
            self.helper(res, child)
        res.append(root.val)