class Solution(object):
    def numberOfWays(self, corridor):
        p = 10 ** 9 + 7
        seatIndices = [i for i in range(len(corridor)) if corridor[i] == "S"]
        numSeats = len(seatIndices)
        
        if numSeats % 2 or numSeats == 0:
            return 0
        
        gapLengths = [seatIndices[i] - seatIndices[i-1] for i in range(2, numSeats, 2)]
        
        numWays = 1
        for i in range(len(gapLengths)):
            numWays *= gapLengths[i]
            
        return numWays % p