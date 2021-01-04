class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # res and stack
        res, stack = [0] * len(T), []

        # go thru temps
        for i in range(len(T)):
            # while there is stuff in stack, AND top of stack < current temp
            while stack and T[stack[-1]] < T[i]:
                # pop stack
                cur = stack.pop()
                # that temp had to wait i - cur days until this temp
                res[cur] = i - cur

            # add this index to stack
            stack.append(i)

        return res