class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        numTrees = defaultdict(int)
        for n in arr:
            numTrees[n] = sum(numTrees[m] * numTrees.get(n//m, 0) for m in arr if n % m == 0) + 1
        return sum(numTrees.values()) % (10**9 + 7)