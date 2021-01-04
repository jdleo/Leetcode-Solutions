from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # buckets for each anagram
        buckets = defaultdict(list)

        # add each string to its bucket
        for s in strs:
            buckets[self.normalize(s)].append(s)

        # simply return the values (buckets)
        return buckets.values()

    # helper function to normalize a word into anagram representation
    def normalize(self, s: str) -> str:
        # char counts
        counts = [0] * 26
        # iter thru string and fill counts
        for char in s:
            counts[ord(char) - ord('a')] += 1
        # return counts arr as string
        return str(counts)