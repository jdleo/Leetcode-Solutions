class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # set of vowels
        vowels = set("aeiouAEIOU")
        # left half vowel count, and right half vowel count
        leftCount = rightCount = 0
        # pointers for left and right
        left, right = 0, len(s) - 1

        # go until pointers meet
        while left < right:
            # increment counts if current chars are vowels
            leftCount += s[left] in vowels
            rightCount += s[right] in vowels

            # pinch the pointers
            left += 1
            right -= 1

        # check if 'alike'
        return leftCount == rightCount