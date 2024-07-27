class Solution(object):
    def firstBadVersion(self, n):
        minIndex = 1
        maxIndex = n
        
        while minIndex < maxIndex:
            midIndex = (minIndex + maxIndex) // 2
            if isBadVersion(midIndex):
                maxIndex = midIndex
            else:
                minIndex = midIndex + 1

        return minIndex