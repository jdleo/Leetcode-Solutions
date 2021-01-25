from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # base case
        if not root: return 0

        # queue for bfs
        queue = deque([root])

        # max value, lowest level, and current level
        mx, res, level = float('-inf'), 0, 1

        # keep going while there are still nodes to traverse
        while queue:
            # get size of queue
            size = len(queue)

            # sum of current level
            sm = 0

            # go thru all nodes on this level
            for _ in range(size):
                cur = queue.popleft()

                # add to cur to sum
                sm += cur.val

                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            # set new max (only if strictly bigger, cuz we want lowest level)
            if sm > mx:
                mx = sm
                res = level

            level += 1

        return res
