class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # for individual char counts
        counts = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        # fill counts
        for move in moves:
            counts[move] += 1

        # make sure up/down and left/right are balanced
        return counts['U'] == counts['D'] and counts['L'] == counts['R']