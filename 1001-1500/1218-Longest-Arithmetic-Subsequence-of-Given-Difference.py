class Solution(object):
    def longestSubsequence(self, arr, difference):
        n = len(arr)
        sequenceLen = defaultdict(int)
        maxLen = 0
        
        for i in range(n):
            currentNum = arr[i]
            currLen = sequenceLen[currentNum - difference] + 1
            sequenceLen[currentNum] = currLen
            maxLen = max(maxLen, currLen)
            
        return maxLen