class Solution(object):
    def minOperations(self, nums):
        numFlips, totalFlips = 0, 0
        flipped = deque()
        
        for i in range(len(nums) - 2):
            if i >= 3:
                numFlips -= flipped.popleft()
            currentFlip = 1 if (numFlips % 2 == nums[i]) else 0
            numFlips += currentFlip
            totalFlips += currentFlip
            flipped.append(currentFlip)
            
        for i in range(len(nums) - 2, len(nums)):
            if i >= 3:
                numFlips -= flipped.popleft()
            if numFlips % 2 == nums[i]:
                return -1
            
        return totalFlips