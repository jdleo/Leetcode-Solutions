class Solution:
    def freqAlphabets(self, s: str) -> str:
        # result string (will be in reverse) as array
        res = []

        # go thru string backwards
        i = len(s) - 1
        while i >= 0:
            # check if this is a character from j-z
            if s[i] == '#':
                # get next two numbers, and merge them
                num = int(s[i-2] + s[i-1])
                # add respective char to res
                res.append(chr(num + ord('a') - 1))
                # skip back 3
                i -= 3
            else:
                # just add respective char to res (it's a-i)
                res.append(chr(int(s[i]) + ord('a') - 1))
                i -= 1

        # reverse and join
        return ''.join(res[::-1])