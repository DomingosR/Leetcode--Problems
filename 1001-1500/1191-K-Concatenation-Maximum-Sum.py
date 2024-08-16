class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        # The following implements Kadane's algorithm
        
        def singleListMaxSum(inputList):
            # If the empty array is not allowed, replace the
            # following line with maxSum = float('-inf')
            maxSum = 0
            currentSum = 0
            
            for num in inputList:
                currentSum = max(num, currentSum + num)
                maxSum = max(maxSum, currentSum)
                
            return maxSum
        
        # Now, consider several cases:
        # (a) If k == 1, the above function suffices;
        # (b) If k == 2, we can simply repeat the list and use the
        #     above function.  The optimal subarray may consist of a suffix
        #     of the original array followed by a prefix of it.
        # (c) If k > 2 and the sum of the array is positive, that sum can
        #.    be repeated (k - 2) times and added to the solution for k == 2.
        
        p = 10 ** 9 + 7
        
        if k == 1:
            return singleListMaxSum(arr)
        
        else:
            auxSum = singleListMaxSum(arr + arr)
            return (auxSum + (k - 2) * max(sum(arr), 0)) % p