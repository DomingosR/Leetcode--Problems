class KthLargest(object):

    def __init__(self, k, nums):
        self.numbers = []
        heapify(self.numbers)
        self.count = 0
        self.k = k
        
        for num in nums:
            if self.count == self.k:
                heappushpop(self.numbers, num)
            else:
                heappush(self.numbers, num)
                self.count += 1
        
    def add(self, val):
        if self.count == self.k:
            heappushpop(self.numbers, val)
        else:
            heappush(self.numbers, val)
            self.count += 1
        return self.numbers[0]