class Solution(object):
    def longestSubarray(self, nums, limit):
        maxDeque = deque()
        minDeque = deque()
        maxLen, leftIndex = 1, 0
        
        for rightIndex in range(len(nums)):
            while maxDeque and maxDeque[-1] < nums[rightIndex]:
                maxDeque.pop()
            maxDeque.append(nums[rightIndex])

            while minDeque and minDeque[-1] > nums[rightIndex]:
                minDeque.pop()
            minDeque.append(nums[rightIndex])
        
            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[leftIndex]:
                    maxDeque.popleft()
                if minDeque[0] == nums[leftIndex]:
                    minDeque.popleft()
                leftIndex += 1
                
            maxLen = max(maxLen, rightIndex - leftIndex + 1)
        
        return maxLen