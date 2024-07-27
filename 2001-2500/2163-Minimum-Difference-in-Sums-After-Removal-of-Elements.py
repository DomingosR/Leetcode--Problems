class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 3

        # Idea: consider each threshold t in the range [n-1, n, n+1, ..., 2n-1].  Compute 
        # the n smallest numbers in [0, 1, ..., t] and the n largest in [t+1, t+2, ... 3n - 1],
        # and take the difference between the two.  Return the smallest such difference.
        
        # Compute minimum left sums
        minLeftSums = [sum(nums[:n])]
        currentLeftSum = sum(nums[:n])
        
        leftHeap = [-nums[i] for i in range(n)]
        heapq.heapify(leftHeap)

        for i in range(n, 2*n):
            incomingNum = nums[i]
            currentHighest = -heapq.heappop(leftHeap)
            nextNum = min(incomingNum, currentHighest)
            currentLeftSum += (nextNum - currentHighest)
            minLeftSums.append(currentLeftSum)
            heapq.heappush(leftHeap, -nextNum)

        # Compute maximum right sums
        maxRightSums = [sum(nums[2*n:])]
        currentRightSum = sum(nums[2*n:])

        rightHeap = [nums[i] for i in range(2*n, 3*n)]
        heapq.heapify(rightHeap)

        for i in range(2*n-1, n-1, -1):
            incomingNum = nums[i]
            currentLowest = heapq.heappop(rightHeap)
            nextNum = max(incomingNum, currentLowest)
            currentRightSum += (nextNum - currentLowest)
            maxRightSums.append(currentRightSum)
            heapq.heappush(rightHeap, nextNum)

        maxRightSums = maxRightSums[::-1]      
        
        # Iterate over pre_min and suf_max and get the minimum difference.
        minDiff = minLeftSums[0] - maxRightSums[0]
        for leftSum, rightSum in zip(minLeftSums, maxRightSums):
            minDiff = min(minDiff, leftSum - rightSum)
        return minDiff