class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        largeNum = 10 ** 5 + 1
        
        heights = list(map(list, zip(*envelopes)))[1]
        auxList = [largeNum] * (len(heights) + 1)
        
        for h in heights:
            auxList[bisect_left(auxList, h)] = h
        
        return auxList.index(largeNum)
        