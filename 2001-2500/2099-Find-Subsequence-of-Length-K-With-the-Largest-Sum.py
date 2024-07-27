class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largestK = []
        heapify(largestK)

        for i in range(k):
            heapq.heappush(largestK, (nums[i], i))

        for i in range(k, len(nums)):
            if nums[i] > largestK[0][0]:
                heapq.heappushpop(largestK, (nums[i], i))

        largestKList = [x for x in largestK]
        largestKList.sort(key = lambda x: x[1])

        return [x[0] for x in largestKList]
