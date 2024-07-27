class Solution(object):
    def maxScore(self, nums1, nums2, k):
        totalScore = 0
        maxScore = 0
        dataHeap = []

        adjData = sorted(list(zip(nums1, nums2)), key=lambda x: -x[1])

        for num1, num2 in adjData:
            heapq.heappush(dataHeap, num1)
            totalScore += num1
            if len(dataHeap) > k:
                totalScore -= heappop(dataHeap)
            if len(dataHeap) == k:
                maxScore = max(maxScore, totalScore * num2)

        return maxScore
