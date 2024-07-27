class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        countPrevious = defaultdict(int)
        numPairs = 0
        
        for n in nums:
            if countPrevious[k-n] > 0:
                numPairs += 1
                countPrevious[k-n] -= 1
            else:
                countPrevious[n] += 1
        
        return numPairs