class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # result fizzbuzz array
        res = []
        # base counters
        base3, base5, base15 = 3, 5, 15

        # iterater from 1 to n
        for i in range(1, n + 1):
            # check if we hit any of the bases
            if i == base15:
                # this means its divisible by 3 and 5
                res.append("FizzBuzz")
                base3, base5, base15 = base3 + 3, base5 + 5, base15 + 15
            elif i == base3:
                res.append("Fizz")
                base3 += 3
            elif i == base5:
                res.append("Buzz")
                base5 += 5
            else:
                res.append(str(i))

        return res