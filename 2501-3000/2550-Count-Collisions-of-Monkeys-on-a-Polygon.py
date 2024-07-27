class Solution(object):
    def monkeyMove(self, n):
        return (pow(2, n, 10 ** 9 + 7) - 2) % (10 ** 9 + 7)