class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        candidates = []

        def process(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(candidates, [nums1[i] + nums2[j], i, j])

        process(0, 0)
        finalPairs = []

        while candidates and len(finalPairs) < k:
            _, i, j = heapq.heappop(candidates)
            finalPairs.append([nums1[i], nums2[j]])
            process(i, j + 1)
            if j == 0:
                process(i + 1, 0)

        return finalPairs
