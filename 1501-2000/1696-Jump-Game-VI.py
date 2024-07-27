def maxScoreV2(nums, k):
        # This version uses a heap to access the maximum value in a range more easily
        n = len(nums)
        queue = []
        maxVal = 0
        for i in range(n):
            maxV = 0
            if queue:
                maxV, indx = queue[0]
                # Pop elements from queue while they are in the permissible range
                while indx + k < i:
                    maxV, indx = heapq.heappop(queue)

                # Push last value back into queue
                heapq.heappush(queue, [maxV, indx])

            # Compute maxVal for arriving at the current number, push back into queue    
            maxVal = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * maxVal, i]) 

        # Last value computed is the optimum value 
        return maxVal

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        return maxScoreV2(nums, k)