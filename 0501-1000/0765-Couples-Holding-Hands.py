class Solution(object):
    def minSwapsCouples(self, row):
        n = len(row) // 2
        numIndices = defaultdict(int)
        
        for i in range(2*n):
            numIndices[row[i]] = i
            
        swapCount = 0
        for i in range(n):
            pair = row[2 * i] + (1 if row[2 * i] % 2 == 0 else -1)
            if row[2 * i + 1] != pair:
                currVal = row[2 * i + 1]
                pairIndex = numIndices[pair]
                row[2 * i + 1], row[pairIndex] = pair, currVal
                numIndices[pair], numIndices[currVal] = 2 * i + 1, pairIndex
                swapCount += 1
        
        return swapCount