class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # sets to hold srcs and destinations
        sources, destinations = set(), set()

        # go through paths
        for src, dst in paths:
            # add source and destination to sets
            sources.add(src)
            destinations.add(dst)

            # if src is in destinations, remove it
            if src in destinations: destinations.remove(src)
            # or, if destination was already in sources
            if dst in sources: destinations.remove(dst)

        # there should only be one left in destination set
        return list(destinations)[0]