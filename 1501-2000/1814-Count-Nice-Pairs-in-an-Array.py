class Solution(object):
    def countNicePairs(self, nums):
        p = 10 ** 9 + 7
        numsAux = [n - int(str(n)[::-1]) for n in nums]
        valueCounter = Counter(numsAux)
        return sum([v * (v - 1) // 2 for v in valueCounter.values()]) % p