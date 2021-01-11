class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # result list of paths
        paths = []
        # start backtracking at starting node (always 0)
        self.backtrack(paths, graph, list(), 0)
        return paths

    # helper backtracking (dfs) function
    def backtrack(self, paths: list[list[int]], graph: list[list[int]],
                  path: list[int], cur: int):
        # reached end
        if cur == len(graph) - 1:
            # add copy of path to paths and break
            paths.append(path + [cur])
        else:
            # add to path, recurse, remove from path
            path.append(cur)

            # go through all neighbor nodes
            for node in graph[cur]:
                # backtrack
                self.backtrack(paths, graph, path, node)

            # remove from path
            path.pop()
