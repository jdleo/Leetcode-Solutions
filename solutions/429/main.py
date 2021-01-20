from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        if not root: return []
        # level by level array, and queue for bfs
        res, queue = [], deque([root])
        # keep going while there are nodes to search
        while queue:
            # get current size of queue and current level
            size, curLevel = len(queue), []
            # poll 'size' times from queue (because this is current level)
            for _ in range(size):
                # poll
                cur = queue.popleft()
                # add to current level
                curLevel.append(cur.val)
                # get children
                for child in cur.children:
                    # add to queue
                    queue.append(child)
            # add current level to result
            res.append(curLevel)

        return res