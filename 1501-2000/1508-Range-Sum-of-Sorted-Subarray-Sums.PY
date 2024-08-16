class Solution(object):
    def rangeSum(self, nums, n, left, right):
        n = len(nums)

        allSums = [(num, i) for i, num in enumerate(nums)]
        heapify(allSums)
        totalSum = 0

        for j in range(1, right + 1):
            currentSum, i = heappop(allSums)
            if j >= left:
                totalSum += currentSum
            if i < n-1:
                heappush(allSums, (currentSum + nums[i+1], i+1))

        return totalSum % (10 ** 9 + 7)