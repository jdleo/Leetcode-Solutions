class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # result number of teams
        res = 0

        # iterate from 1 to length - 1 (middle soldier)
        for i in range(1, len(rating) - 1):
            # less and greater arrays
            less, greater = [0] * 2, [0] * 2
            # iterate thru ratings (for left and right soldiers)
            for j in range(len(rating)):

                if rating[i] < rating[j]:
                    # increment less[0] if i < j
                    less[0 if i < j else 1] += 1

                if rating[j] < rating[i]:
                    # increment greater[0] if i < j
                    greater[0 if i < j else 1] += 1

            # add teams to res
            res += less[0] * greater[1] + less[1] * greater[0]

        return res