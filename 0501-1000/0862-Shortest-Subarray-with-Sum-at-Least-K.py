class Solution(object):
    def shortestSubarray(self, nums, k):
        # For the elements in this deque, first entry is the
        # index of the cumulative sum, the second is the sum itself.
        # Elements are kept in decreasing order of the sum.
        cumSumDeque = deque([[-1, 0]])
    
        minLen = float('inf')
        curSum = 0
        
        for i, num in enumerate(nums):
            curSum += num
            
            # If the sum in the last element of the deque is at least
            # the current sum minus k, we found a subarray of sum k,
            # so consider it as a candidate.  We can discard the last
            # element, since it will not be the endpoint of any optimal
            # subarray from this point on
            while cumSumDeque and curSum - cumSumDeque[-1][1] >= k:
                minLen = min(minLen, i - cumSumDeque.pop()[0])
                
            # We can also discard any early elements of the array with sum
            # greater than the current, as they are suboptimal from this point on
            while cumSumDeque and curSum <= cumSumDeque[0][1]:
                cumSumDeque.popleft()
                
            # Finally, include the current sum for future consideration
            cumSumDeque.appendleft([i, curSum])
            
        return -1 if minLen == float('inf') else minLen