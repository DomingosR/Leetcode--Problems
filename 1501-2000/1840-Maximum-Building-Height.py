class Solution(object):
    def maxBuilding(self, n, restrictions):
        def maxHeightBetween(i, j, heightI, heightJ):
            maxLimitHeight = max(heightI, heightJ)
            diffIndices = abs(j - i) - abs(heightJ - heightI)
            return maxLimitHeight + (diffIndices // 2)

        numRestrictions = len(restrictions)
        if numRestrictions == 0:
             return n-1

        restrictions.sort(key = lambda(x): x[0])

        if restrictions[0][0] > 1:
            numRestrictions += 1
            restrictions = [[1, 0]] + restrictions

        if restrictions[-1][0] < n:
            numRestrictions += 1
            maxHeightLastBuilding = restrictions[-1][1] + (n - restrictions[-1][0])
            restrictions = restrictions + [[n, maxHeightLastBuilding]]

        for i in range(1, numRestrictions):
            indexDiff = restrictions[i][0] - restrictions[i-1][0]
            propagateLimit = restrictions[i-1][1] + indexDiff
            restrictions[i][1] = min(restrictions[i][1], propagateLimit)
        
        for i in range(numRestrictions - 2, -1, -1):
            indexDiff = restrictions[i+1][0] - restrictions[i][0]
            propagateLimit = restrictions[i+1][1] + indexDiff
            restrictions[i][1] = min(restrictions[i][1], propagateLimit)

        maxHeight = 0
        for i in range(numRestrictions - 1):
            index1 = restrictions[i][0]
            index2 = restrictions[i+1][0]
            height1 = restrictions[i][1]
            height2 = restrictions[i+1][1]           
            maxHeight = max(maxHeight, maxHeightBetween(index1, index2, height1, height2))

        return maxHeight