class Solution(object):
    def numTrees(self, n):
        prevValues = defaultdict(int)
        prevValues[0] = 1
        prevValues[1] = 1
        prevValues[2] = 2
        prevValues[3] = 5
        
        def computeNumTrees(num):
            if num not in prevValues:
                computedVal = 0
                for i in range(num):
                    computedVal += computeNumTrees(i) * computeNumTrees(num-i-1)
                prevValues[num] = computedVal
                
            return prevValues[num]
        
        return computeNumTrees(n)