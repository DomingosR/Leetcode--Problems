class Solution(object):
    def findKthLargest(self, nums, k):
        numHeap = nums[:k]
        heapq.heapify(numHeap)

        for i in range(k, len(nums)):
            heapq.heappushpop(numHeap, nums[i])

        return numHeap[0]