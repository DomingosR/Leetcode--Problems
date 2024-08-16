class Solution(object):
    def addNegabinary(self, arr1, arr2):
        if arr1 == [0] and arr2 == [0]:
            return [0]
        
        totalLen = max(len(arr1), len(arr2))
        totalSum = [0] * totalLen
        
        for i in range(totalLen):
            totalSum[i] = (arr1[-i-1] if i < len(arr1) else 0) + (arr2[-i-1] if i < len(arr2) else 0)
           
        i = 0
        while i < len(totalSum):
            if totalSum[i] > 1:
                if i == len(totalSum) - 1:
                    totalSum.append(0)
                while totalSum[i] >= 2 and totalSum[i+1] >= 1:
                    totalSum[i] -= 2
                    totalSum[i+1] -= 1
                if totalSum[i] >= 2:
                    if i == len(totalSum) - 2:
                        totalSum.append(0)
                    while totalSum[i] >= 2:
                        totalSum[i] -= 2
                        totalSum[i+1] += 1
                        totalSum[i+2] += 1
            i += 1
        
        while totalSum and totalSum[-1] == 0:
            totalSum.pop()
        
        if not totalSum:
            return [0]
        
        return totalSum[::-1]