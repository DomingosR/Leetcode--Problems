class Solution(object):
    def minimumDeviation(self, nums):
        maxVal = 10**9 + 1
        numsHeap = []
        minNum = maxVal

        for n in nums:
            if n % 2 == 1:
                n *= 2
            minNum = min(minNum, n)
            heappush(numsHeap, -n)

        minDiff = -numsHeap[0] - minNum

        while -numsHeap[0] % 2 == 0:
            currentNum = -heappop(numsHeap)
            nextNum = currentNum // 2
            minNum = min(minNum, nextNum)
            heappush(numsHeap, -nextNum)
            minDiff = min(-numsHeap[0] - minNum, minDiff)
        
        return minDiff