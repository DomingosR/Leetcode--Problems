class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        numTests = minutesToTest // minutesToDie
        maxBuckets, numPigs = 1, 0
        while maxBuckets < buckets:
            maxBuckets *= (1 + numTests)
            numPigs += 1
        return numPigs