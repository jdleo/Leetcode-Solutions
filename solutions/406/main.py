class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort people first by height descending, then by order
        people.sort(key=lambda x: (-x[0], x[1]))

        # queue to reconstruct
        queue = []

        # iterate thru people
        for person in people:
            # simply insert person at k
            queue.insert(person[1], person)

        return queue