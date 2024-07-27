class Solution(object):
    def longestIdealString(self, s, k):
        maxLen = [0] * 26
        
        for char in s:
            i = ord(char) - ord("a")
            maxLen[i] = max(maxLen[max(i-k, 0) : min(i+k+1, 26)]) + 1
        
        return max(maxLen)