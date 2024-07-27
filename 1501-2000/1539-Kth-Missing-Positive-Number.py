class Solution(object):
    def findKthPositive(self, arr, k):
        leftVal = 0
        rightVal = len(arr)

        while leftVal < rightVal:
            midVal = (leftVal + rightVal) // 2
            if arr[midVal] < k + midVal + 1:
                leftVal = midVal + 1
            else:
                rightVal = midVal
        
        return leftVal + k