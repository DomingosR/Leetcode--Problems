class Solution(object):
    def mostCompetitive(self, nums, k):
        n = len(nums)
        finalSubseq = []
        
        for i, num in enumerate(nums):
            while finalSubseq and finalSubseq[-1] > num and len(finalSubseq) + (n - i) >= k + 1:
                finalSubseq.pop()
            if len(finalSubseq) < k:
                finalSubseq.append(num)
                
        return finalSubseq