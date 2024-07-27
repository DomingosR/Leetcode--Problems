class Solution(object):
    def longestArithSeqLength(self, nums):
        longestSeq = defaultdict(int)
        n = len(nums)
        maxLen = 2
        
        for i in range(n-1):
            for j in range(i+1, n):
                if (i, nums[j]-nums[i]) in longestSeq:
                    longestSeq[(j, nums[j]-nums[i])] = longestSeq[(i, nums[j]-nums[i])] + 1
                    maxLen = max(maxLen, longestSeq[(j, nums[j]-nums[i])])
                else:
                    longestSeq[(j, nums[j]-nums[i])] = 2
                
        return maxLen