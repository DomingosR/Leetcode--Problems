class Solution(object):
    def countTriplets(self, arr):
        cumXOR = 0
        cumVals = defaultdict(list)
        cumVals[0].append(-1)
        totalCount = 0
        
        for i in range(len(arr)):
            cumXOR ^= arr[i]
            if cumXOR in cumVals:
                for j in cumVals[cumXOR]:
                    totalCount += (i - j - 1)
            cumVals[cumXOR].append(i)
            
        return totalCount