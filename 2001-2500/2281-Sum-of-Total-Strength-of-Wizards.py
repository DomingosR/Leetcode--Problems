class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        p = 10 ** 9 + 7
        n = len(strength)
        
        # For each i, find bounds of arrays for which strength[i] is the minimum.
        # To account for the possibility of repeated values, we specify that
        # strength[i] is the last occurrence of this minimum.
        
        prevSmaller = [-1] * n
        auxStack = []
        
        for i in range(n):
            while auxStack and strength[auxStack[-1]] >= strength[i]:
                auxStack.pop()
            if auxStack:
                prevSmaller[i] = auxStack[-1]
            auxStack.append(i)
            
        nextSmallerOrEqual = [n] * n
        auxStack = []
        
        for i in range(n-1, -1, -1):
            while auxStack and strength[auxStack[-1]] > strength[i]:
                auxStack.pop()
            if auxStack:
                nextSmallerOrEqual[i] = auxStack[-1]
            auxStack.append(i)
            
        # Compute the accumulation of values in the list
        cumSum = list(accumulate(strength))
        cumSum2 = list(accumulate(cumSum))
        
        # Compute total strength
        totalStrength = 0
        
        for i in range(n):
            prevIndex, nextIndex = prevSmaller[i], nextSmallerOrEqual[i]
            term1 = (i - prevIndex) * (cumSum2[nextIndex - 1] - (cumSum2[i - 1] if i > 0 else 0))
            term2 = (nextIndex - i) * (cumSum2[i - 1] if i > 0 else 0)
            term3 = (nextIndex - i) * (cumSum2[prevIndex - 1] if prevIndex > 0 else 0)
            totalStrength += (term1 - term2 + term3) * strength[i]
            
        return totalStrength % p