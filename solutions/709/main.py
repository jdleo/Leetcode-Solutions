class Solution:
    def toLowerCase(self, str: str) -> str:
        # result array of chars
        res = []

        # iter thru str
        for char in str:
            # check if this is an uppercase character
            if ord('A') <= ord(char) <= ord('Z'):
                # add its lowercase version to res
                res.append(chr(ord(char) + 32))
            else:
                # just add this char
                res.append(char)

        # join back res
        return ''.join(res)