class MedianFinder(object):
    
    def __init__(self):
        self.lowerHalf = []
        self.upperHalf = []
        
    def addNum(self, num):
        if len(self.lowerHalf) == 0:
            heapq.heappush(self.lowerHalf, -num)
        else:
            if len(self.lowerHalf) - len(self.upperHalf) == 1:
                maxLower = -self.lowerHalf[0]
                if num >= maxLower:
                    heapq.heappush(self.upperHalf, num)
                else:
                    heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))
                    heapq.heappush(self.lowerHalf, -num)
            else:
                minUpper = self.upperHalf[0]
                if num <= minUpper:
                    heapq.heappush(self.lowerHalf, -num)
                else:
                    heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))
                    heapq.heappush(self.upperHalf, num)
   
                
    def findMedian(self):
        maxLower = -self.lowerHalf[0]
        if len(self.lowerHalf) - len(self.upperHalf) == 1:
            return maxLower
        else:
            minUpper = self.upperHalf[0]
            return 1.0 * (maxLower + minUpper) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()