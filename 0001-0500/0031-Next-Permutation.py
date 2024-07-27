class Solution(object):
    def nextPermutation(self, nums):
        numValues = len(nums)

        # Traverse array backwards, find the first point at which numbers decrease
        i = numValues - 1
        targetIndex= -1

        while i >= 1 and targetIndex < 0:
            if nums[i-1] < nums[i]:
                targetIndex = i-1
            else:
                i -= 1

        if targetIndex == -1:
            # Array is in decreasing order, so must reverse it and return it
            i = 0
            j = numValues - 1
            while i < j:
                auxVal = nums[i]
                nums[i] = nums[j]
                nums[j] = auxVal
                i += 1
                j -= 1

        else:
            # Find smallest number to the right of targetIndex which is higher
            # than inputArray[targetIndex]
            i = targetIndex + 1
            while i < numValues - 1 and nums[i+1] > nums[targetIndex]:
                i += 1

            # Swap values at targetIndex and i
            auxVal = nums[targetIndex]
            nums[targetIndex] = nums[i]
            nums[i] = auxVal

            # Reverse order of array to the right of targetIndex
            i = targetIndex + 1
            j = numValues - 1
            while i < j:
                auxVal = nums[i]
                nums[i] = nums[j]
                nums[j] = auxVal
                i += 1
                j -= 1
