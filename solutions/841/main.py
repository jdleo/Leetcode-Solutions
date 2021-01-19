class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        if not rooms: return True

        # stack for DFS and visited set
        stack, visited = [0], set([0])

        # keep going while nodes to traverse
        while stack:
            # pop cur
            cur = stack.pop()
            # go thru children of cur
            for child in rooms[cur]:
                # check if not already visited
                if child not in visited:
                    # add to visited, and stack
                    stack.append(child)
                    visited.add(child)

        # check if visited all rooms - simple
        return len(visited) == len(rooms)