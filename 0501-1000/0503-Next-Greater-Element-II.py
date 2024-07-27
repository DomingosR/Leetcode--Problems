class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        numsAux = nums + nums

        nextGreater = [-1] * (2 * n)
        indexStack = []
        
        for i in range(2 * n - 1, -1, -1):
            while indexStack and numsAux[i] >= numsAux[indexStack[-1]]:
                indexStack.pop()
            if indexStack:
                nextGreater[i] = numsAux[indexStack[-1]]
            indexStack.append(i)
            
        return nextGreater[:n]