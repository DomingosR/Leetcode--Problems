class Solution(object):
    def minKBitFlips(self, nums, k):
        numFlips, totalFlips = 0, 0
        flipped = deque()
        
        for i in range(len(nums) - k + 1):
            if i >= k:
                numFlips -= flipped.popleft()
            currentFlip = 1 if (numFlips % 2 == nums[i]) else 0
            numFlips += currentFlip
            totalFlips += currentFlip
            flipped.append(currentFlip)
            
        for i in range(len(nums) - k + 1, len(nums)):
            if i >= k:
                numFlips -= flipped.popleft()
            if numFlips % 2 == nums[i]:
                return -1
            
        return totalFlips