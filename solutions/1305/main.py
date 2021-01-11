from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # queues for elements, and result array
        q1, q2, res = deque(), deque(), []

        # fill queues with inorder lists from root1 and root2
        self.inorder(root1, q1)
        self.inorder(root2, q2)

        # while both queues have values to merge
        while q1 and q2:
            # add minimum value and pop from queue
            res.append(q1.popleft() if q1[0] < q2[0] else q2.popleft())

        # one of these queues will be empty, so itll just be concating an empty list anyways
        # so this is fine to do
        return res + list(q1) + list(q2)

    # helper method to build inorder list
    def inorder(self, root: TreeNode, queue: deque):
        if root:
            self.inorder(root.left, queue)
            queue.append(root.val)
            self.inorder(root.right, queue)
