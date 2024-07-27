class Solution(object):
    def topKFrequent(self, nums, k):
        auxVals = Counter(nums).most_common(k)
        return[a for a, b in auxVals]
