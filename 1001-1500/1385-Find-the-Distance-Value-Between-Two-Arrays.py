class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        numElements = 0
        
        for num in arr1:
            if num < arr2[0] - d or num > arr2[-1] + d:
                numElements += 1
            else:
                index = bisect_left(arr2, num)
                if 1 <= index <= len(arr2) - 1 and arr2[index - 1] + d < num < arr2[index] - d:
                    numElements += 1
        
        return numElements