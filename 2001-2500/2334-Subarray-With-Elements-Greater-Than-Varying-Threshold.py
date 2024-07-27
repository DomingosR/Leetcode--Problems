class Solution(object):
    def validSubarraySize(self, nums, threshold):
        def prevSmaller(inputList):
            n = len(inputList)
            auxQueue = []
            prevIndex = [-1] * n

            for i, num in enumerate(inputList):
                while auxQueue and inputList[auxQueue[-1]] >= num:
                    auxQueue.pop()
                if auxQueue:
                    prevIndex[i] = auxQueue[-1]
                auxQueue.append(i)

            return prevIndex

        def nextSmaller(inputList):
            n = len(inputList)
            auxQueue = []
            nextIndex = [n] * n

            for i in range(n-1, -1, -1):
                num = inputList[i]
                while auxQueue and inputList[auxQueue[-1]] >= num:
                    auxQueue.pop()
                if auxQueue:
                    nextIndex[i] = auxQueue[-1]
                auxQueue.append(i)

            return nextIndex
        
        n = len(nums)
        prevIndex, nextIndex = prevSmaller(nums), nextSmaller(nums)
        
        for i in range(n):
            arrLen = nextIndex[i] - prevIndex[i] - 1
            if arrLen * nums[i] > threshold:
                return arrLen
            
        return -1