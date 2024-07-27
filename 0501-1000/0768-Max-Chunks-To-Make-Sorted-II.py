class Solution(object):
    def maxChunksToSorted(self, arr):
        arr2 = sorted(arr)
        
        numChunks = 0
        originalDict, sortedDict = defaultdict(int), defaultdict(int)
        
        for i in range(len(arr)):
            originalDict[arr[i]] += 1
            sortedDict[arr2[i]] += 1
            if originalDict == sortedDict:
                numChunks += 1
                originalDict, sortedDict = defaultdict(int), defaultdict(int)
        
        return numChunks