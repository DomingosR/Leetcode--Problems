class Solution(object):
    def kthGrammar(self, n, k):
        numChanges, k = 0, k-1
        for _ in range(n):
            numChanges += (k % 2)
            k //= 2
        return numChanges % 2