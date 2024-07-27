class Solution(object):
    def passThePillow(self, n, time): 
        k = time % (2 * (n-1))
        return k + 1 if k < n else 2 * n - k - 1