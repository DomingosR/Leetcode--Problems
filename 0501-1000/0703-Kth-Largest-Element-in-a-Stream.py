class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.KNums = []
        heapq.heapify(self.KNums)
        
        for i in range(len(nums)):
            if i < self.k:
                heapq.heappush(self.KNums, nums[i])
            else:
                self.add(nums[i])

    def add(self, val):
        if self.k > len(self.KNums):
            heapq.heappush(self.KNums, val)
        elif val > self.KNums[0]:
            heapq.heappushpop(self.KNums, val)
        return self.KNums[0]