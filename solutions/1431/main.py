class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # get max candy holder
        maxCandies = max(candies)

        # return mapping of candies, where true/false 
        # if adding extra candies would make it greater than max
        return list(map(lambda candy: candy + extraCandies >= maxCandies, candies))