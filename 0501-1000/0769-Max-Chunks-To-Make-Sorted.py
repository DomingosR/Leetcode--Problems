class Solution(object):
    def maxChunksToSorted(self, arr):
        numChunks = 0
        maxCurrentChunk = -1
        
        for i in range(len(arr)):
            maxCurrentChunk = max(maxCurrentChunk, arr[i])
            if maxCurrentChunk == i:
                numChunks += 1
                maxCurrentChunk = -1
                
        return numChunks