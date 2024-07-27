class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        numCounter = Counter(arr)
        valueCounter = [val for val in numCounter.values()]
        valueCounter.sort(key = lambda x: -x)
        
        while valueCounter and k > 0:
            k -= valueCounter.pop()
            
        return len(valueCounter) + (1 if k < 0 else 0)