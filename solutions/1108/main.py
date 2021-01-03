class Solution:
    def defangIPaddr(self, address: str) -> str:
        # result array of chars
        res = []

        # iterate thru ip address
        for char in address:
            # append brackets if period, char if not
            if char == '.': res.append('[.]')
            else: res.append(char)

        # join array to string result
        return ''.join(res)
