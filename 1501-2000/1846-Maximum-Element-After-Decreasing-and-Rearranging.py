class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr = [0] + arr
        
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        
        return arr[-1]
            