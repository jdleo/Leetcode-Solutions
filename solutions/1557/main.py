class Solution:
    def findSmallestSetOfVertices(self, n: int,
                                  edges: List[List[int]]) -> List[int]:
        # set of all possible nodes (assume every node has an indegree)
        nodes = {i for i in range(n)}

        # go thru edges
        for _, dst in edges:
            # check if destination is in nodes
            if dst in nodes:
                # that means it now has in-degree > 0, remove it
                nodes.remove(dst)

        # result is all nodes left with in-degree 0
        return list(nodes)