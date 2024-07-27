class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        minHeap = []
        
        for i in range(n):
            for j in range(i+1, n):
                heappush(minHeap, (1.0 * arr[i] / arr[j], (arr[i], arr[j])))
                
        for _ in range(k):
            num1, num2 = heappop(minHeap)[1]
            
        return [num1, num2]