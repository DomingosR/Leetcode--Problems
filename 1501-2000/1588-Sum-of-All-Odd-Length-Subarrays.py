class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n, totalSum = len(arr), 0
        
        def numEven(m):
            return m//2 + 1
        
        def numOdd(m):
            return (m-1)//2 + 1
            
        for i, num in enumerate(arr):
            totalSum += arr[i] * (numEven(i) * numEven(n-i-1) + numOdd(i) * numOdd(n-i-1))
        
        return totalSum