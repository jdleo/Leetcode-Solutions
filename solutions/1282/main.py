from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # buckets of people per group size
        buckets = defaultdict(list)

        # go through group sizes
        for person, groupSize in enumerate(groupSizes):
            # add to corresponding bucket
            buckets[groupSize].append(person)

        # result array
        res = []

        # go through each group bucket
        for groupSize, people in buckets.items():
            # go through number of people / group size
            for i in range(len(people) // groupSize):
                # add this chunk to res
                res.append(people[i*groupSize: i*groupSize + groupSize])

        return res