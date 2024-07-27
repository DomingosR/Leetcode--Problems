class Solution(object):
    def combine(self, n, k):
        if k == 0:
            return [[]]

        return [prev + [i] for i in range(k, n+1) for prev in self.combine(i-1, k-1)]
